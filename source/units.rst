Magnetic Unit Converter
=======================

.. raw:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Magnetic Unit Converter</title>
    <style>
        body {
        font-family: Arial, sans-serif;
        background: #f4f4f4;
        margin: 0;
        padding: 20px;
        }
        .converter-container {
        max-width: 500px;
        margin: 40px auto;
        background: #fff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h2 {
        text-align: center;
        margin-bottom: 20px;
        }
        .input-group,
        .result-group {
        margin-bottom: 20px;
        }
        label {
        display: block;
        margin: 10px 0 5px;
        font-weight: bold;
        }
        input[type="number"],
        select,
        input[type="text"] {
        width: 100%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 1em;
        }
        input[readonly] {
        background-color: #e9ecef;
        cursor: text;
        }
        .group-container {
        display: flex;
        justify-content: space-between;
        gap: 20px;
        flex-wrap: wrap;
        }
        fieldset {
        flex: 1;
        min-width: 200px;
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 10px 15px 15px;
        }
        legend {
        font-weight: bold;
        padding: 0 5px;
        }
    </style>
    </head>
    <body>
    <div class="converter-container">
        <h2>Magnetic Unit Converter</h2>
        <div class="input-group">
        <label for="inputValue">Enter Value:</label>
        <input type="number" id="inputValue" placeholder="Enter value" step="any" />
        </div>
        <div class="group-container">
        <fieldset>
            <legend>From</legend>
            <label for="fromPrefix">Prefix:</label>
            <select id="fromPrefix"></select>
            <label for="fromUnit">Unit:</label>
            <select id="fromUnit"></select>
        </fieldset>
        <fieldset>
            <legend>To</legend>
            <label for="toPrefix">Prefix:</label>
            <select id="toPrefix"></select>
            <label for="toUnit">Unit:</label>
            <select id="toUnit"></select>
        </fieldset>
        </div>
        <div class="result-group">
        <label for="result">Result:</label>
        <input type="text" id="result" readonly />
        </div>
    </div>

    <script>
        // Permeability of free space
        const mu0 = 4 * Math.PI * 1e-7;

        // Available prefixes – default (none) is represented by the empty string.
        const prefixes = {
        "": 1,
        "p": 1e-12,
        "n": 1e-9,
        "µ": 1e-6,
        "m": 1e-3,
        "k": 1e3,
        "M": 1e6,
        "G": 1e9
        };
        // Order in which prefixes appear (none first).
        const prefixOrder = ["p", "n", "µ", "m", "", "k", "M", "G"];

        // Base magnetic units.
        const baseUnits = ["T", "G", "A/m", "Oe"];

        /*  
        Conversion factors between base units.
        */
        const conversionFactor = {
        "T": {
            "T": 1,
            "G": 1e4,
            "A/m": 1 / mu0,
            "Oe": 1e4
        },
        "G": {
            "T": 1e-4,
            "G": 1,
            "A/m": 1e-4 / mu0,
            "Oe": 1
        },
        "A/m": {
            "T": mu0,
            "G": mu0 * 1e4,
            "A/m": 1,
            "Oe": 1e4 * mu0
        },
        "Oe": {
            "T": 1e-4,
            "G": 1,
            "A/m": 1e-4 / mu0,
            "Oe": 1
        }
        };

        /**
        * Convert a number into a string of Unicode superscript characters.
        * For example, formatSuperscript(-12) returns "⁻¹²".
        */
        function formatSuperscript(n) {
        const superscriptMap = {
            "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴",
            "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹", "-": "⁻"
        };
        return n.toString().split('').map(c => superscriptMap[c] || c).join('');
        }

        /**
        * Populate a prefix dropdown with options using the format:
        *   For nonempty prefixes: "p (×10⁻¹²)" for example.
        *   For the empty prefix, display as "None (×10⁰)".
        */
        function populatePrefixDropdown(selectId) {
        const select = document.getElementById(selectId);
        select.innerHTML = "";
        prefixOrder.forEach(prefix => {
            const multiplier = prefixes[prefix];
            // Since all multipliers are powers of 10, compute exponent:
            const exponent = Math.round(Math.log10(multiplier));
            const formattedMultiplier = `×10${formatSuperscript(exponent)}`;
            const displayText = (prefix === "" ? "None" : prefix) + " (" + formattedMultiplier + ")";
            const option = new Option(displayText, prefix);
            select.add(option);
        });
        }

        // Populate the base unit dropdown.
        function populateUnitDropdown(selectId) {
        const select = document.getElementById(selectId);
        select.innerHTML = "";
        baseUnits.forEach(unit => {
            const option = new Option(unit, unit);
            select.add(option);
        });
        }

        /**
        * Format the output value.
        *
        * - For identity conversions (same base unit and prefix), match the input’s decimal places.
        * - For non-identity conversions, use full precision.
        */
        function formatOutput(inputStr, finalValue, isIdentityConversion) {
        if (isIdentityConversion) {
            let decimals = 0;
            if (inputStr.includes('.')) {
            decimals = inputStr.split('.')[1].length;
            }
            return finalValue.toFixed(decimals);
        } else {
            return finalValue.toString();
        }
        }

        // Perform the conversion and update the result field.
        function convertUnits() {
        const inputElem = document.getElementById("inputValue");
        const inputStr = inputElem.value;
        const inputValue = parseFloat(inputStr);
        const resultField = document.getElementById("result");

        if (isNaN(inputValue)) {
            resultField.value = "";
            return;
        }

        // Get the selected prefixes and base units.
        const fromPrefix = document.getElementById("fromPrefix").value;
        const fromUnit = document.getElementById("fromUnit").value;
        const toPrefix = document.getElementById("toPrefix").value;
        const toUnit = document.getElementById("toUnit").value;

        // Check that the conversion factor exists.
        if (!conversionFactor[fromUnit] || conversionFactor[fromUnit][toUnit] === undefined) {
            resultField.value = `Conversion from ${fromUnit} to ${toUnit} is not supported.`;
            return;
        }

        // Conversion steps:
        // 1. Multiply by the "from" prefix multiplier.
        // 2. Convert between base units.
        // 3. Divide by the "to" prefix multiplier.
        const valueInBase = inputValue * prefixes[fromPrefix];
        const convertedBaseValue = valueInBase * conversionFactor[fromUnit][toUnit];
        const finalValue = convertedBaseValue / prefixes[toPrefix];

        // Determine if this is an identity conversion.
        const isIdentity = (fromUnit === toUnit && fromPrefix === toPrefix);
        const formattedResult = formatOutput(inputStr, finalValue, isIdentity);

        // Display the result in a format that is easy to copy.
        resultField.value = `${formattedResult} ${toPrefix}${toUnit}`;
        }

        // Attach event listeners to update the conversion automatically.
        function attachEventListeners() {
        document.getElementById("inputValue").addEventListener("input", convertUnits);
        document.getElementById("fromPrefix").addEventListener("change", convertUnits);
        document.getElementById("fromUnit").addEventListener("change", convertUnits);
        document.getElementById("toPrefix").addEventListener("change", convertUnits);
        document.getElementById("toUnit").addEventListener("change", convertUnits);
        }

        // Initialize dropdowns and event listeners once the DOM is loaded.
        document.addEventListener("DOMContentLoaded", () => {
        populatePrefixDropdown("fromPrefix");
        populatePrefixDropdown("toPrefix");
        populateUnitDropdown("fromUnit");
        populateUnitDropdown("toUnit");

        // Set default prefix to "None" (empty string) for both sides.
        document.getElementById("fromPrefix").value = "";
        document.getElementById("toPrefix").value = "";

        attachEventListeners();
        convertUnits(); // Perform an initial conversion (if any value exists)
        });
    </script>
    </body>
    </html>
