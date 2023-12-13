#!/usr/bin/node
exports.esrever = function (list) {
  let left, right, tmp;
  left = 0;
  right = list.length - 1;

  while (left < right) {
    tmp = list[left];
    list[left] = list[right];
    list[right] = tmp;
    right--;
    left++;
  }
  return list;
};
