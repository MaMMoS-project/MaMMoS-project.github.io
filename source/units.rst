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
      /* Your CSS styles */
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
      h2 { text-align: center; margin-bottom: 20px; }
      .input-group, .result-group { margin-bottom: 20px; }
      label { display: block; margin: 10px 0 5px; font-weight: bold; }
      input[type="number"], select, input[type="text"] {
         width: 100%; padding: 10px; border: 1px solid #ccc;
         border-radius: 5px; font-size: 1em;
      }
      input[readonly] { background-color: #e9ecef; cursor: text; }
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
      legend { font-weight: bold; padding: 0 5px; }
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

   <!-- Adjust the src attribute to the correct path.
         For example, if magneticConverter.js is in your _static folder,
         use: <script src="_static/magneticConverter.js"></script> -->
   <script src="_static/magneticConverter.js"></script>
   <script>
      // Ensure the module loaded successfully.
      if (!window.magneticConverter) {
         console.error("magneticConverter not loaded. Please check the file path.");
      }

      // Populate the dropdowns.
      function populatePrefixDropdown(selectId) {
         var select = document.getElementById(selectId);
         select.innerHTML = "";
         
         // Define the order in which prefixes appear.
         var prefixOrder = ["p", "n", "µ", "m", "", "k", "M", "G"];

         // Mapping for superscript conversion
         const superscriptMap = {
            "-": "⁻", "0": "⁰", "1": "¹", "2": "²", "3": "³",
            "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹"
         };

         prefixOrder.forEach(function(prefix) {
            var multiplier = window.magneticConverter.prefixes[prefix];
            var exponent = Math.round(Math.log10(multiplier));

            // Convert exponent to superscript using mapping
            var formattedExponent = [...exponent.toString()].map(char => superscriptMap[char] || char).join("");
            var formattedMultiplier = "×10" + formattedExponent; // Proper superscript formatting

            var displayText = (prefix === "" ? "None" : prefix) + " (" + formattedMultiplier + ")";
            var option = new Option(displayText, prefix);
            select.add(option);
         });
      }


      function populateUnitDropdown(selectId) {
         var select = document.getElementById(selectId);
         select.innerHTML = "";
         window.magneticConverter.baseUnits.forEach(function(unit) {
         var option = new Option(unit, unit);
         select.add(option);
         });
      }

      function convertUnits() {
         var inputElem = document.getElementById("inputValue");
         var inputValue = parseFloat(inputElem.value);
         var resultField = document.getElementById("result");

         if (isNaN(inputValue)) {
         resultField.value = "";
         return;
         }

         var fromPrefix = document.getElementById("fromPrefix").value;
         var fromUnit = document.getElementById("fromUnit").value;
         var toPrefix = document.getElementById("toPrefix").value;
         var toUnit = document.getElementById("toUnit").value;

         try {
         var finalValue = window.magneticConverter.convertUnit(inputValue, fromPrefix, fromUnit, toPrefix, toUnit);
         resultField.value = finalValue + " " + (toPrefix === "" ? "" : toPrefix) + toUnit;
         } catch (e) {
         resultField.value = e.message;
         }
      }

      function attachEventListeners() {
         document.getElementById("inputValue").addEventListener("input", convertUnits);
         document.getElementById("fromPrefix").addEventListener("change", convertUnits);
         document.getElementById("fromUnit").addEventListener("change", convertUnits);
         document.getElementById("toPrefix").addEventListener("change", convertUnits);
         document.getElementById("toUnit").addEventListener("change", convertUnits);
      }

      document.addEventListener("DOMContentLoaded", function() {
         populatePrefixDropdown("fromPrefix");
         populatePrefixDropdown("toPrefix");
         populateUnitDropdown("fromUnit");
         populateUnitDropdown("toUnit");

         // Set default values.
         document.getElementById("fromPrefix").value = "";
         document.getElementById("toPrefix").value = "";

         attachEventListeners();
         convertUnits();
      });
   </script>
   </body>
   </html>

This magnetic unit converter allows you to convert between different magnetic units. Simply enter a value, select the units you want to convert from and to, and the converter will display the result.

Unit Details
------------

Below are details of the magnetic units available in this converter:

- **T (Tesla)**: The SI unit for magnetic flux density.
- **G (Gauss)**: The CGS unit for magnetic flux density.
- **A/m (Ampere per meter)**: The SI unit for magnetic field strength.
- **Oe (Oersted)**: The CGS unit for magnetic field strength.

**Conversion Note:**  
All unit conversions in this app are performed assuming a relative permeability (μᵣ) of 1. This assumption treats the medium as non-magnetic (e.g., free space or vacuum).