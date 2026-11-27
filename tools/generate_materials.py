"""Generate the materials pages from a local checkout of MaMMoS-project/uppsala-data.

Usage: pixi run python tools/generate_materials.py UPPSALA_DATA_DIR [MATERIAL ...]

Writes ``source/materials/index.rst`` and one page per material. Without
MATERIAL arguments every dataset in ``UPPSALA_DATA_DIR/data`` is processed.
"""

import argparse
import json
import re
from pathlib import Path

import mammos_analysis
import mammos_entity as me
import numpy as np
from bokeh.embed import json_item
from bokeh.layouts import column
from bokeh.models import (BoxZoomTool, ColumnDataSource, CrosshairTool, HoverTool, Label, Node, PanTool,
                          Range1d, ResetTool, Span, Title, WheelZoomTool, ZoomInTool, ZoomOutTool)
from bokeh.palettes import Category10_10 as PALETTE
from bokeh.plotting import figure
from bokeh.themes import Theme, built_in_themes

REPO_URL = "https://github.com/MaMMoS-project/uppsala-data"
OUT_DIR = Path(__file__).resolve().parent.parent / "source" / "materials"

SYMBOLS = {"Ms": "M_s", "Js": "J_s", "Ku": "K_u", "Tc": "T_c", "K1": "K_1"}
CHART_SYMBOLS = {"Ms": "Mₛ", "Cv": "Cᵥ", "chi": "χ", "A": "A", "K1": "K₁", "U_L": "Uₗ"}
# Columns of UppASD/MC_1/thermal.csv shown as charts: (name, title, skip T=0).
# UppASD reports a meaningless susceptibility at T = 0, which would dominate the axis.
SPIN_DYNAMICS_CHARTS = [
    ("Ms", "Spontaneous magnetization", False),
    ("Cv", "Isochoric heat capacity", False),
    ("chi", "Magnetic susceptibility", True),
]
KUZMIN_STEP = 1  # K, spacing of the temperatures at which the fit is charted
KUZMIN_TABLE_STEP = 10  # K, spacing of the rows of the fit table
BINDER_WINDOW = 50  # K either side of Tc in the default view of the Binder cumulant chart
# Set via themes: a model attribute set to its default value (13px axis labels) would lose to dark_minimal's sizes.
FONTS = {"Axis": {"major_label_text_font_size": "12px", "axis_label_text_font_size": "13px"}}
DARK = built_in_themes["dark_minimal"]._json["attrs"]
THEMES = {"light": Theme(json={"attrs": FONTS}),
          "dark": Theme(json={"attrs": DARK | {"Axis": DARK["Axis"] | FONTS["Axis"]}})}


def formula_rst(name):
    """Return the dataset name as rst with subscripted counts and the suffix in brackets."""
    formula, _, suffix = name.partition("_")
    rst = re.sub(r"(\d+(?:\.\d+)?)", r"\ :sub:`\1`\ ", formula).rstrip("\\ ")
    return f"{rst} ({suffix.replace('_', ' ')})" if suffix else rst


def symbol_rst(key):
    """Return a property symbol such as ``Ms`` as rst with a subscript."""
    base, _, sub = SYMBOLS.get(key, key).partition("_")
    return f"{base}\\ :sub:`{sub}`" if sub else base


def unit_text(unit):
    """Return a unit in compact form, e.g. ``MJ / m3`` -> ``MJ/m³``."""
    return str(unit).replace(" / ", "/").replace("m3", "m³").replace("m2", "m²")


def join_numbers(values, unit):
    """Return numbers with ``unit`` as a comma-separated list with at most four decimals."""
    return ", ".join(f"{v:.4f}".rstrip("0").rstrip(".") + unit for v in values)


def cell_row(cif_text):
    """Return lattice parameters and cell volume of a CIF as one table row."""
    # Values may carry an uncertainty in brackets, e.g. "5.7192(9)".
    values = {k: float(v) for k, v in re.findall(r"^_cell_(\w+)\s+([-\d.]+)", cif_text, re.MULTILINE)}
    lengths = [values[f"length_{k}"] for k in "abc"]
    angles = [values[f"angle_{k}"] for k in ("alpha", "beta", "gamma")]
    ca, cb, cg = np.cos(np.radians(angles))
    volume = np.prod(lengths) * np.sqrt(1 - ca**2 - cb**2 - cg**2 + 2 * ca * cb * cg)
    return [join_numbers(lengths, " Å"), join_numbers(angles, "°"), f"{volume:.2f} Å³"]


def list_table(header, rows, widths):
    """Return an rst list-table; a cell may hold several paragraphs separated by blank lines."""
    lines = [".. list-table::", "   :header-rows: 1", f"   :widths: {widths}", ""]
    for row in [header, *rows]:
        for i, cell in enumerate(row):
            first, *rest = cell.split("\n")
            lines.append(f"   {'*' if i == 0 else ' '} - {first}".rstrip())
            lines += [f"       {line}".rstrip() for line in rest]
    return "\n".join(lines)


def raw_html(html):
    """Return an rst raw-html directive containing ``html``."""
    body = "\n".join(f"   {line}" if line else "" for line in html.splitlines())
    return f".. raw:: html\n\n{body}\n"


def series(label, kind, x, y):
    """Return one chart series as plain lists."""
    return {"label": label, "kind": kind, "x": [float(v) for v in x], "y": [float(v) for v in y]}


def chart(key, title, unit, marker, data, note=""):
    """Return the description of one chart."""
    return {"title": title, "symbol": CHART_SYMBOLS[key], "unit": unit_text(unit), "note": note,
            "marker": marker, "series": data}


def spin_dynamics_charts(thermal, tc):
    """Return the charts of the UppASD temperature sweep."""
    marker = {"x": tc, "label": f"Tc = {tc:g} K"}
    charts = []
    for key, title, skip_t0 in SPIN_DYNAMICS_CHARTS:
        q = thermal[key].q
        keep = thermal.T.value > 0 if skip_t0 else np.full(q.shape, True)
        data = [series("UppASD", "line", thermal.T.value[keep], q.value[keep])]
        charts.append(chart(key, title, q.unit, marker, data, "T = 0 K omitted" if skip_t0 else ""))
    return charts


def binder_chart(runs, tc):
    """Return the chart of the Binder cumulants of the Monte Carlo runs, viewed around ``tc``."""
    marker = {"x": tc, "label": f"Tc = {tc:g} K"}
    data = [series(label, "line", thermal.T.value, thermal.U_L.value) for label, thermal in runs]
    xrange = [tc - BINDER_WINDOW, tc + BINDER_WINDOW]
    return {**chart("U_L", "Binder cumulant", "", marker, data, "near Tc"), "xrange": xrange}


def kuzmin_charts(fit, thermal):
    """Return the charts of Ms, A and K1 from a Kuz'min fit."""
    t_max = thermal.T.value.max()
    temps = np.union1d(np.arange(0, t_max + KUZMIN_STEP, KUZMIN_STEP), thermal.T.value)
    tc = fit.Tc.value
    marker = {"x": tc, "label": f"Tc (fit) = {tc:.0f} K"}
    ms = fit.Ms(temps).q.to(thermal.Ms.q.unit)
    a = fit.A(temps).q.to("pJ/m")
    k1 = fit.K1(temps).q.to("MJ/m3")
    return [
        chart("Ms", "Spontaneous magnetization", ms.unit, marker, [
            series("Kuz'min fit", "line", temps, ms.value),
            series("UppASD", "points", thermal.T.value, thermal.Ms.value),
        ]),
        chart("A", "Exchange stiffness", a.unit, marker, [series("Kuz'min fit", "line", temps, a.value)]),
        chart("K1", "Anisotropy constant", k1.unit, marker, [series("Kuz'min fit", "line", temps, k1.value)]),
    ]


def padded(lo, hi):
    """Return the range lo..hi widened by 5 % on each side."""
    d = 0.05 * (hi - lo)
    return Range1d(lo - d, hi + d)


def bokeh_figure(c, hairline, x_range, markers):
    """Return chart ``c`` as a Bokeh figure sharing the section's hairline span and default x range.

    ``markers`` marks the data points of line series (the simulated temperatures).
    """
    series = c["series"]
    if xr := c.get("xrange"):
        inside = [y for s in series for x, y in zip(s["x"], s["y"]) if xr[0] <= x <= xr[1]]
        x_range, y_range = Range1d(*xr), padded(min(inside), max(inside))
    else:
        ys = [y for s in series for y in s["y"]]
        y_range = padded(min(0, *ys), max(0, *ys))
    ylabel = c["symbol"] + (f" ({c['unit']})" if c["unit"] else "")
    f = figure(frame_height=240, sizing_mode="stretch_width", x_range=x_range, y_range=y_range,
               x_axis_label="Temperature (K)", y_axis_label=ylabel,
               background_fill_color=None, border_fill_color=None, outline_line_color=None,
               tools=[PanTool(), BoxZoomTool(), ZoomInTool(factor=0.4), ZoomOutTool(factor=0.4),
                      WheelZoomTool(), ResetTool(), CrosshairTool(overlay=hairline, visible=False)])
    # Wheel zoom starts off so the page scrolls over charts; its toolbar button switches it on.
    f.toolbar.active_scroll = None
    if c["note"]:
        f.add_layout(Title(text=c["note"], text_font_size="12px", text_font_style="italic"), "above")
    f.add_layout(Title(text=c["title"], text_font_size="14px"), "above")
    multi = len(series) > 1
    for i, s in enumerate(series):
        kw = {"legend_label": s["label"]} if multi else {}
        if s["kind"] == "points":
            f.scatter(s["x"], s["y"], size=6, color=PALETTE[i], **kw)
        else:
            f.line(s["x"], s["y"], line_width=2, color=PALETTE[i], **kw)
            if markers:
                f.scatter(s["x"], s["y"], size=4, color=PALETTE[i], **kw)
    m = c["marker"]
    f.add_layout(Span(location=m["x"], dimension="height", line_dash="dashed", line_color="gray"))
    f.add_layout(Label(x=m["x"], y=Node(target="frame", symbol="top"), x_offset=4, y_offset=-4, text=m["label"],
                       text_font_size="12px", text_baseline="top", text_color="gray"))
    if multi:
        f.legend.location = "bottom_left"
        f.legend.background_fill_alpha = 0
    # Hover table of the line series, one row per temperature: each row gets an invisible full-height quad
    # reaching halfway to its neighbours, so the tooltip shows the nearest temperature and follows the
    # cursor (for line glyphs Bokeh pins it to the curve).
    lines = [(i, s) for i, s in enumerate(series) if s["kind"] == "line"]
    temps = sorted({x for _, s in lines for x in s["x"]})
    table = {"T": temps}
    for i, s in lines:
        values = dict(zip(s["x"], s["y"]))
        table[f"s{i}"] = [f"{values[t]:.4g} {c['unit']}".strip() if t in values else "" for t in temps]
    mid = [(a + b) / 2 for a, b in zip(temps, temps[1:])]
    table["x0"] = [-1e9] + mid
    # A cursor exactly on a shared edge would match both quads and list both rows; the tiny gap prevents that.
    table["x1"] = [v - 1e-6 * abs(v) for v in mid] + [1e9]
    r = f.quad(left="x0", right="x1", bottom=-1e30, top=1e30, source=ColumnDataSource(table),
               fill_alpha=0, line_alpha=0)
    labels = [c["symbol"] if len(lines) == 1 else s["label"] for _, s in lines]
    f.add_tools(HoverTool(renderers=[r], visible=False, point_policy="follow_mouse",
                          tooltips=[("T", "@T{0.[0]} K")] + [(lab, f"@s{i}") for lab, (i, _) in zip(labels, lines)]))
    return f


def charts_html(charts, markers=False):
    """Return a section's charts stacked in one column: a container and its light and dark Bokeh items."""
    hairline = Span(dimension="height", line_color="gray", line_width=1)
    shared = Range1d(0, max(x for c in charts if "xrange" not in c for s in c["series"] for x in s["x"]))
    layout = column([bokeh_figure(c, hairline, shared, markers) for c in charts], sizing_mode="stretch_width")
    items = json.dumps({name: json_item(layout, theme=theme) for name, theme in THEMES.items()})
    # Prevent the data from closing the surrounding <script> element.
    items = items.replace("</", "<\\/")
    return f'<div class="mammos-charts"></div><script type="application/json">{items}</script>'


def data_table(summary, columns):
    """Return a collapsible HTML table; ``columns`` holds (header HTML, unit, values) triples."""
    head = "".join(f"<th>{label}{f' ({unit})' if unit else ''}</th>" for label, unit, _ in columns)
    rows = "\n".join(
        "<tr>" + "".join(f"<td>{values[i]:g}</td>" for _, _, values in columns) + "</tr>"
        for i in range(len(columns[0][2]))
    )
    return (
        f'<details class="mammos-data-table"><summary>{summary}</summary>\n'
        f'<table class="table"><thead><tr>{head}</tr></thead>\n<tbody>\n{rows}\n</tbody></table></details>'
    )


def thermal_table(thermal):
    """Return a collapsible table of the UppASD data shown in the charts."""
    cols = [("T", "T"), ("Ms", "M<sub>s</sub>"), ("Js", "J<sub>s</sub>"), ("Cv", "C<sub>v</sub>"), ("chi", "χ")]
    return data_table("Show data as a table",
                      [(label, unit_text(thermal[k].q.unit), thermal[k].value) for k, label in cols])


def binder_table(runs):
    """Return a collapsible table of the Binder cumulants; all runs share one temperature grid."""
    columns = [("T", "K", runs[0][1].T.value)]
    columns += [(f"U<sub>L</sub> {label}", "", thermal.U_L.value) for label, thermal in runs]
    return data_table("Show Binder cumulants as a table", columns)


def kuzmin_rows(fit, props):
    """Return the Kuz'min fit parameters as rows of the entity table."""
    a0, k0 = fit.A(0).q.to("pJ/m"), props.Ku
    return [
        [symbol_rst("Tc"), f":entity:`{fit.Tc.ontology_label}`", f"{fit.Tc.value:.4g} K", "fitted to M\\ :sub:`s`\\ (T)"],
        ["s", "Kuz'min shape parameter", f"{fit.s.value:.4g}", "fitted to M\\ :sub:`s`\\ (T)"],
        ["A(0)", f":entity:`{fit.A(0).ontology_label}`", f"{a0.value:.4g} {unit_text(a0.unit)}", "from M\\ :sub:`s`\\ (0), T\\ :sub:`c` and s (Kuz'min)"],
        [f"{symbol_rst('K1')}\\ (0)", f":entity:`{fit.K1(0).ontology_label}`", f"{k0.value:.4g} {unit_text(k0.q.unit)}",
         f"input: {symbol_rst('Ku')} from DFT"],
    ]


def kuzmin_table(fit):
    """Return a collapsible table of the fitted Ms, A and K1 from 0 K to Tc."""
    temps = np.arange(0, fit.Tc.value, KUZMIN_TABLE_STEP)
    ms, a, k1 = fit.Ms(temps).q, fit.A(temps).q.to("pJ/m"), fit.K1(temps).q.to("MJ/m3")
    return data_table("Show fit values as a table", [
        ("T", "K", temps),
        ("M<sub>s</sub>", unit_text(ms.unit), ms.value),
        ("A", unit_text(a.unit), a.value),
        ("K<sub>1</sub>", unit_text(k1.unit), k1.value),
    ])


def run_label(run_dir):
    """Return the run name with its system size from inpsd.dat, e.g. "MC_1 (30×30×30)"."""
    words = next(w for w in map(str.split, (run_dir / "inpsd.dat").read_text().splitlines()) if w[:1] == ["ncell"])
    return f"{run_dir.name} ({'×'.join(words[1:4])})"


def material_page(name, props, cif_text, runs, fit):
    """Return the rst source of one material page; ``runs`` holds (label, thermal) per MC directory."""
    title = formula_rst(name)
    thermal = runs[0][1]
    spin_charts = spin_dynamics_charts(thermal, props.Tc.value)
    tables = thermal_table(thermal)
    # Several system sizes: Tc comes from the crossing of their Binder cumulants.
    if len(runs) > 1:
        spin_charts.append(binder_chart(runs, props.Tc.value))
        tables += "\n" + binder_table(runs)
    # Prevent the CIF text from closing the surrounding <script> element.
    payload = json.dumps({"cif": cif_text}).replace("</", "<\\/")
    prop_rows = [
        [symbol_rst(k), f":entity:`{e.ontology_label}`", f"{e.value:g} {unit_text(e.q.unit)}", e.description]
        for k, e in props
    ]
    csv_url = f"{REPO_URL}/blob/main/data/{name}/UppASD/MC_1/thermal.csv"

    return f"""\
.. Generated by tools/generate_materials.py; do not edit by hand.

{title}
{"=" * len(title)}

.. raw:: html

   <script defer src="../_static/bokeh.min.js"></script>
   <script defer src="../_static/materials.js"></script>
   <script type="application/json" id="mammos-material-data">{payload}</script>

Dataset: `uppsala-data/data/{name} <{REPO_URL}/tree/main/data/{name}>`__

Unit cell
---------

{raw_html(f'<div class="mammos-structure" role="region" aria-label="Interactive crystal structure of {name}">'
           '<p class="mammos-placeholder">Loading the 3D structure viewer…</p></div>')}
Lattice parameters from `structure.cif <{REPO_URL}/blob/main/data/{name}/structure.cif>`__:

{list_table(["a, b, c", "α, β, γ", "V"], [cell_row(cif_text)], "auto")}

Intrinsic properties
--------------------

{list_table(["Symbol", "Property", "Value", "Note"], prop_rows, "10 40 20 30")}

Temperature dependence: spin dynamics
-------------------------------------

The dashed line marks T\\ :sub:`c` = {props.Tc.value:g} K;
`thermal.csv <{csv_url}>`__ holds all computed columns.

{raw_html(charts_html(spin_charts, markers=True) + chr(10) + tables)}
Kuz'min fit
-----------

{list_table(["Symbol", "Property", "Value", "Note"], kuzmin_rows(fit, props), "10 40 20 30")}

{raw_html(charts_html(kuzmin_charts(fit, thermal)) + chr(10) + kuzmin_table(fit))}"""


def index_page(names, rows):
    """Return the rst source of the materials overview page."""
    table = list_table(
        ["Material", "T\\ :sub:`c` (K)", "M\\ :sub:`s` (kA/m)", "J\\ :sub:`s` (T)",
         "K\\ :sub:`u` (MJ/m³)"],
        rows,
        "28 18 18 18 18",
    )
    toctree = "\n".join(f"   {name}" for name in names)
    return f"""\
.. Generated by tools/generate_materials.py; do not edit by hand.

Materials
=========

Intrinsic magnetic properties of materials computed within MaMMoS at Uppsala
University. The raw inputs and outputs are in
`MaMMoS-project/uppsala-data <{REPO_URL}>`__.

.. toctree::
   :hidden:

{toctree}

{table}

Methods
-------

All materials were computed with the same workflow:

- **DFT with RSPt** for the magnetic ground state, the uniaxial anisotropy
  constant K\\ :sub:`u`, and the exchange parameters J\\ :sub:`ij` used in
  the spin-dynamics model. K\\ :sub:`u` is the energy difference between
  calculations with the magnetization along x and z, obtained either with the
  force theorem or from total energies; the note on each material page says
  which.
- **Monte Carlo simulations with UppASD** give the temperature dependence of
  the magnetization, heat capacity and susceptibility. T\\ :sub:`c` is taken
  from the peak in the heat capacity or, where several system sizes were
  simulated, from the crossing of their Binder cumulants.
- **Kuz'min fit** with
  `mammos-analysis <https://mammos-project.github.io/mammos/examples/mammos-analysis/quickstart.html#mammos-analysis-kuzmin>`__:
  the Kuz'min formula is fitted to M\\ :sub:`s`\\ (T) from UppASD, which yields
  T\\ :sub:`c`, the shape parameter s, and the temperature dependence of the
  exchange stiffness A and of K\\ :sub:`1`, starting from K\\ :sub:`1`\\ (0) =
  K\\ :sub:`u`.
"""


def main():
    """Parse arguments and write all pages."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("data_repo", type=Path, help="checkout of uppsala-data")
    parser.add_argument("materials", nargs="*", help="dataset names (default: all)")
    args = parser.parse_args()

    data_dir = args.data_repo / "data"
    names = args.materials or sorted(p.name for p in data_dir.iterdir() if p.is_dir())
    OUT_DIR.mkdir(exist_ok=True)
    index_rows = []
    for name in names:
        src = data_dir / name
        props = me.from_yaml(src / "intrinsic_properties.yaml")
        # Tc from a Binder cumulant crossing always uses MC_1 and MC_2; further runs are ignored.
        run_dirs = [d for d in (src / "UppASD" / f"MC_{i}" for i in (1, 2)) if d.is_dir()]
        runs = [(run_label(d), me.from_csv(d / "thermal.csv")) for d in run_dirs]
        thermal = runs[0][1]
        fit = mammos_analysis.kuzmin_properties(T=thermal.T, Ms=thermal.Ms, K1_0=props.Ku)
        cif_text = (src / "structure.cif").read_text()
        (OUT_DIR / f"{name}.rst").write_text(material_page(name, props, cif_text, runs, fit))
        index_rows.append([f":doc:`{name}`"] + [f"{props[k].value:g}" for k in ("Tc", "Ms", "Js", "Ku")])
    (OUT_DIR / "index.rst").write_text(index_page(names, index_rows))


if __name__ == "__main__":
    main()
