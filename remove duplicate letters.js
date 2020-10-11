// 316. Remove Duplicate Letters
// Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

// Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

// Example 1:

// Input: s = "bcabc"
// Output: "abc"
// Example 2:

// Input: s = "cbacdcbc"
// Output: "acdb"

// Constraints:

// 1 <= s.length <= 104
// s consists of lowercase English letters.

const removeDuplicateLetters = function (s) {
  const last = {};
  for (let i = 0; i < s.length; i++) {
    last[s[i]] = i;
  }
  const stack = [];
  const seen = new Set();
  for (let i = 0; i < s.length; i++) {
    let c = s[i];
    if (seen.has(c)) continue;
    while (
      stack.length > 0 &&
      stack[stack.length - 1] > c &&
      last[stack[stack.length - 1]] > i
    ) {
      seen.delete(stack.pop());
    }
    stack.push(c);
    seen.add(c);
  }

  return stack.join("");
};
