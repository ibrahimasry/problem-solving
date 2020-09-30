// 41. First Missing Positive

// Given an unsorted integer array, find the smallest missing positive integer.

// Example 1:

// Input: [1,2,0]
// Output: 3
// Example 2:

// Input: [3,4,-1,1]
// Output: 2
// Example 3:

// Input: [7,8,9,11,12]
// Output: 1
// Follow up:

// Your algorithm should run in O(n) time and uses constant extra space.

const firstMissingPositive = function (nums) {
  let i = 0;

  while (i < nums.length) {
    let target = nums[i] - 1;
    if (target >= 0 && target < nums.length && nums[target] !== nums[i]) {
      [nums[i], nums[target]] = [nums[target], nums[i]];
    } else {
      i++;
    }
  }

  for (let i = 0; i < nums.length; i++) if (i + 1 !== nums[i]) return i + 1;
  return nums.length + 1;
};
