#!/usr/bin/node
exports.converter = function (base) {
  function doConvertion (num) {
    return num.toString(base);
  }
  return doConvertion;
};
