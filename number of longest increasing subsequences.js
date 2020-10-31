// Number of Longest Increasing Subsequence

// Given an integer array nums, return the number of longest increasing subsequences.

// Example 1:

// Input: nums = [1,3,5,4,7]
// Output: 2
// Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
// Example 2:

// Input: nums = [2,2,2,2,2]
// Output: 5
// Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

// Constraints:

// 0 <= nums.length <= 2000
// -106 <= nums[i] <= 106

var findNumberOfLIS = function (nums) {
  if (nums.length == 0) return 0;
  let dp = Array(nums.length).fill(1);
  let count = Array(nums.length).fill(1);

  let max = 1;
  let res = 0;
  for (let i = 1; i < nums.length; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[j] < nums[i]) {
        if (dp[i] < dp[j] + 1) {
          dp[i] = dp[j] + 1;
          count[i] = count[j];
        } else if (dp[i] == dp[j] + 1) {
          count[i] += count[j];
        }
      }

      if (dp[i] > max) {
        max = dp[i];
      }
    }
  }

  for (let i = 0; i < dp.length; i++) {
    if (dp[i] == max) res += count[i];
  }
  return res;
};
