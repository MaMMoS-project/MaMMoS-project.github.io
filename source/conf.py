# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MaMMoS'
copyright = '2023, MaMMos collaboration'
author = 'MaMMos collaboration'

import sys
from pathlib import Path

import bokeh.util.paths

sys.path.insert(0, str(Path(__file__).parent / "_ext"))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.githubpages',  # creates .nojekyll file in HTML directory
    'sphinxcontrib.email', 
    'sphinx_design',
    'mammos_entity_role',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_logo = '_static/mammos-logo.png'
html_favicon = '_static/mammos-favicon.png'
# BokehJS from the installed bokeh, which also writes the chart JSON, so their versions always match.
html_static_path = ['_static', str(Path(bokeh.util.paths.bokehjs_path()) / 'js' / 'bokeh.min.js')]
html_css_files = ['vendor/tippy/tippy.css', 'entity.css', 'materials.css']
html_js_files = [
    'vendor/tippy/popper.min.js',
    'vendor/tippy/tippy-bundle.umd.min.js',
    'entity_tippy_click.js',
]
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/mammos-project",
            "icon": "fab fa-github-square",
        },
    ],
    "show_prev_next": False,
    "header_links_before_dropdown": 6,
    "secondary_sidebar_items": ["page-toc"],
}
# Exact page names take precedence over the wildcard, so list the materials pages.
html_sidebars = {
    "**": [],  # by default no left sidebar
    **{
        f"materials/{rst.stem}": ["sidebar-nav-bs"]
        for rst in (Path(__file__).parent / "materials").glob("*.rst")
    },
}
