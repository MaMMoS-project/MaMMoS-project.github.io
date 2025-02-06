(function () {
  // Physical constant: permeability of free space.
  var mu0 = 4 * Math.PI * 1e-7;

  // Prefix multipliers.
  var prefixes = {
    "": 1,
    "p": 1e-12,
    "n": 1e-9,
    "µ": 1e-6,
    "m": 1e-3,
    "k": 1e3,
    "M": 1e6,
    "G": 1e9
  };

  // Base magnetic units.
  var baseUnits = ["T", "G", "A/m", "Oe"];

  // Conversion factors between base units.
  var conversionFactor = {
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
   * Converts a value from one magnetic unit (with prefix) to another.
   *
   * @param {number} inputValue - The numerical value to convert.
   * @param {string} fromPrefix - The prefix for the input unit (e.g., "", "m", "k").
   * @param {string} fromUnit - The base input unit (e.g., "T", "G").
   * @param {string} toPrefix - The prefix for the output unit.
   * @param {string} toUnit - The base output unit.
   * @returns {number} - The converted value.
   */
  function convertUnit(inputValue, fromPrefix, fromUnit, toPrefix, toUnit) {
    if (isNaN(inputValue)) {
      throw new Error("Invalid input value");
    }
    if (!conversionFactor[fromUnit] || conversionFactor[fromUnit][toUnit] === undefined) {
      throw new Error("Conversion from " + fromUnit + " to " + toUnit + " is not supported.");
    }
    // Convert input value to base unit, apply conversion, then remove target prefix.
    return (inputValue * prefixes[fromPrefix] *
            conversionFactor[fromUnit][toUnit]) /
           prefixes[toPrefix];
  }

  // Build the magneticConverter object.
  var magneticConverter = {
    convertUnit: convertUnit,
    prefixes: prefixes,
    baseUnits: baseUnits,
    conversionFactor: conversionFactor
  };

  // Attach magneticConverter to module.exports (if available) and to globalThis.
  if (typeof module !== "undefined" && module.exports) {
    module.exports = magneticConverter;
  }
  globalThis.magneticConverter = magneticConverter;
})();
