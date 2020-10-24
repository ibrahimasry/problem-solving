// leetcode 456. 132 Pattern
// Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

// Return true if there is a 132 pattern in nums, otherwise, return false.

// Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?

// Example 1:

// Input: nums = [1,2,3,4]
// Output: false
// Explanation: There is no 132 pattern in the sequence.
// Example 2:

// Input: nums = [3,1,4,2]
// Output: true
// Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
// Example 3:

// Input: nums = [-1,3,2,0]
// Output: true
// Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

/**
 * @param {number[]} nums
 * @return {boolean}
 */
const find132pattern = function (nums) {
  const min = [...nums];
  // compute 1 in the pattern
  for (let i = 1; i < nums.length; i++) {
    min[i] = Math.min(min[i], min[i - 1]);
  }

  const stack = [];
  // compute 2 in the pattern by mono increasing stack
  for (let i = nums.length - 1; i >= 0; i--) {
    let curr = nums[i];
    let next;
    while (stack.length && curr > stack[stack.length - 1]) next = stack.pop();
    if (next && min[i] < next) return true;
    stack.push(curr);
  }

  return false;
};
