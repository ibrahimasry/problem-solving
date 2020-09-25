// leetcode 179. Largest Number

// Given a list of non negative integers, arrange them such that they form the largest number.

// Example 1:

// Input: [10,2]
// Output: "210"
// Example 2:

// Input: [3,30,34,5,9]
// Output: "9534330"
// Note: The result may be very large, so you need to return a string instead of an integer.

const largestNumber = function (nums) {
  const res = nums.sort((a, b) => (`${a}${b}` > `${b}${a}` ? -1 : 1)).join("");

  return res[0] == "0" ? "0" : res;
};
