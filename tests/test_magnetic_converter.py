import math
from pathlib import Path
import execjs  # PyExecJS
import pytest
import itertools
import mammosunits as u

u.set_enabled_equivalencies(u.magnetic_flux_field())

BASE_DIR = Path(__file__).resolve().parent.parent
JS_FILE_PATH = BASE_DIR / "source" / "_static" / "magneticConverter.js"

with JS_FILE_PATH.open("r", encoding="utf-8") as f:
    js_code = f.read()

# Compile the JavaScript code using ExecJS.
ctx = execjs.compile(js_code)

baseunits = ["T", "G", "A/m", "Oe"]
prefixes = ["", "p", "n", "µ", "m", "k", "M", "G"]
values = [1, math.pi]

# Generate all possible (unit, prefix) combinations
unit_combinations = list(itertools.product(prefixes, baseunits))

# Create conversion test cases by pairing each unit combination with every other
test_cases = [
    (value, from_prefix, from_unit, to_prefix, to_unit)
    for value, (from_prefix, from_unit), (to_prefix, to_unit) in itertools.product(
        values, unit_combinations, unit_combinations
    )
]

test_cases.extend(
    [
        (0, "", "T", "", "G"),  # Zero value conversion
    ]
)


@pytest.mark.parametrize(
    "input_value, from_prefix, from_unit, to_prefix, to_unit", test_cases
)
def test_conversion(input_value, from_prefix, from_unit, to_prefix, to_unit):
    # Build the JavaScript call string.
    # Note: The UMD module attaches our conversion function to "magneticConverter".
    js_call = (
        f"magneticConverter.convertUnit({input_value}, '{from_prefix}', "
        f"'{from_unit}', '{to_prefix}', '{to_unit}')"
    )
    result = ctx.eval(js_call)
    expected = (
        (input_value * u.Unit(f"{from_prefix}{from_unit}"))
        .to(f"{to_prefix}{to_unit}")
        .value
    )
    assert math.isclose(
        result, expected, rel_tol=1e-5
    ), f"Converting {input_value} {from_prefix}{from_unit} to {to_prefix}{to_unit}: expected {expected}, got {result}"


@pytest.mark.parametrize(
    "input_value, from_prefix, from_unit, to_prefix, to_unit, expected_error",
    [
        (1, "", "Unknown", "", "G", "Conversion from Unknown to G is not supported."),
        (1, "", "T", "", "Unknown", "Conversion from T to Unknown is not supported."),
        ("abc", "", "T", "", "G", "Invalid input value"),
    ],
)
def test_conversion_errors(
    input_value, from_prefix, from_unit, to_prefix, to_unit, expected_error
):
    js_call = (
        f"magneticConverter.convertUnit({repr(input_value)}, '{from_prefix}', "
        f"'{from_unit}', '{to_prefix}', '{to_unit}')"
    )
    with pytest.raises(Exception) as excinfo:
        ctx.eval(js_call)
    assert expected_error in str(excinfo.value)
