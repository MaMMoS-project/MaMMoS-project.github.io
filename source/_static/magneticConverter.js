(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define([], factory);
  } else if (typeof module === 'object' && module.exports) {
    // Node/CommonJS
    module.exports = factory();
    // Also attach to globalThis so it can be used as a global in a browser.
    globalThis.magneticConverter = module.exports;
  } else {
    // Browser globals (root is window)
    root.magneticConverter = factory();
  }
}(typeof self !== 'undefined' ? self : this, function () {
  // --- Begin Conversion Code ---
  var mu0 = 4 * Math.PI * 1e-7;

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

  var baseUnits = ["T", "G", "A/m", "Oe"];

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
   * Converts an input value from one unit (with prefix) to another.
   *
   * @param {number} inputValue - The numerical value to convert.
   * @param {string} fromPrefix - The prefix for the input unit (e.g. "", "m", "k").
   * @param {string} fromUnit - The base input unit (e.g. "T", "G").
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
    // 1. Apply the “from” prefix.
    var valueInBase = inputValue * prefixes[fromPrefix];
    // 2. Convert between base units.
    var convertedBaseValue = valueInBase * conversionFactor[fromUnit][toUnit];
    // 3. Remove the “to” prefix.
    var finalValue = convertedBaseValue / prefixes[toPrefix];
    return finalValue;
  }
  // --- End Conversion Code ---

  // Expose the functions and constants.
  return {
    convertUnit: convertUnit,
    prefixes: prefixes,
    baseUnits: baseUnits,
    conversionFactor: conversionFactor
  };
}));
