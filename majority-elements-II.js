// problem link : https://leetcode.com/problems/majority-element-ii/
// Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

// Note: The algorithm should run in linear time and in O(1) space.

// Example 1:

// Input: [3,2,3]
// Output: [3]

const majorityElement = function (nums) {
  let first, second;
  let firstCount = 0;
  let secondCount = 0;
  for (let n of nums) {
    if (first == n || (firstCount == 0 && n != second)) {
      first = n;
      firstCount++;
    } else if (secondCount == 0 || second == n) {
      second = n;
      secondCount++;
    } else {
      secondCount--;
      firstCount--;
    }
  }
  const count = { [first]: 0, [second]: 0 };
  for (let n of nums) {
    if (firstCount > 0 && n == first) count[first]++;
    if (secondCount > 0 && n == second) count[second]++;
  }
  return [first, second].filter((e) => count[e] > Math.floor(nums.length / 3));
};
