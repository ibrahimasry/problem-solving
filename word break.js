//leetcode  139. Word Break

// The same word in the dictionary may be reused multiple times in the segmentation.
// You may assume the dictionary does not contain duplicate words.
// Example 1:

// Input: s = "leetcode", wordDict = ["leet", "code"]
// Output: true
// Explanation: Return true because "leetcode" can be segmented as "leet code".
// Example 2:

// Input: s = "applepenapple", wordDict = ["apple", "pen"]
// Output: true
// Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
//              Note that you are allowed to reuse a dictionary word.
// Example 3:

// Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
// Output: false

const wordBreak = function (s, wordDict) {
  const set = new Set(wordDict);

  return helper(s, set, 0, {});
};

function helper(s, set, start, cache) {
  if (start === s.length) return true;
  if (cache[start] === false) return false;

  for (let i = start; i < s.length; i++) {
    if (!set.has(s.slice(start, i + 1))) continue;
    if (helper(s, set, i + 1, cache)) return true;
  }
  cache[start] = false;
  return false;
}
