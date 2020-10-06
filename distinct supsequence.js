// leetcode 115. Distinct Subsequences

// Given a string S and a string T, count the number of distinct subsequences of S which equals T.

// A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

// It's guaranteed the answer fits on a 32-bit signed integer.

// Example 1:

// Input: S = "rabbbit", T = "rabbit"
// Output: 3
// Explanation:
// As shown below, there are 3 ways you can generate "rabbit" from S.
// (The caret symbol ^ means the chosen letters)

// rabbbit
// ^^^^ ^^
// rabbbit
// ^^ ^^^^
// rabbbit
// ^^^ ^^^
// Example 2:

// Input: S = "babgbag", T = "bag"
// Output: 5
// Explanation:
// As shown below, there are 5 ways you can generate "bag" from S.
// (The caret symbol ^ means the chosen letters)

// babgbag
// ^^ ^
// babgbag
// ^^    ^
// babgbag
// ^    ^^
// babgbag
//   ^  ^^
// babgbag
//     ^^^
//O(n) space , O(n * m) time
const numDistinct = function (s, t) {
  let dp = Array(s.length + 1).fill(1);

  for (let i = 1; i < t.length + 1; i++) {
    let curr = Array(s.length + 1).fill(0);
    for (let j = 1; j < s.length + 1; j++) {
      if (s[j - 1] == t[i - 1]) curr[j] = dp[j - 1] + curr[j - 1];
      else curr[j] = curr[j - 1];
    }
    dp = curr;
  }

  return dp[dp.length - 1];
};

//recursion witn memo
//O(n * m) space , O(n * m) time

const numDistinct2 = function (s, t) {
  return helper(s, t, 0, 0, {});
};

function helper(s, t, i, j, cache) {
  if (j == t.length) return 1;
  if (i == s.length) return 0;
  const idx = i + "-" + j;
  if (idx in cache) return cache[idx];
  let res = 0;
  if (s[i] == t[j]) res = helper(s, t, i + 1, j + 1, cache);

  res += helper(s, t, i + 1, j, cache);
  cache[idx] = res;
  return res;
}
