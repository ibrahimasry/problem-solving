// 520. Detect Capital

// Given a word, you need to judge whether the usage of capitals in it is right or not.

// We define the usage of capitals in a word to be right when one of the following cases holds:

// All letters in this word are capitals, like "USA".
// All letters in this word are not capitals, like "leetcode".
// Only the first letter in this word is capital, like "Google".
// Otherwise, we define that this word doesn't use capitals in a right way.

// Example 1:

// Input: "USA"
// Output: True

// Example 2:

// Input: "FlaG"
// Output: False

// Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

const isCapital = (c) =>
  c.charCodeAt() >= "A".charCodeAt() && c.charCodeAt() <= "Z".charCodeAt();
var detectCapitalUse = function (word) {
  let capital = 0;

  for (let i = 0; i < word.length; i++) {
    let c = word[i];
    const curr = isCapital(c);
    if (curr && i == capital) capital++;
    else if (curr && capital < i + 1) return false;
    else if (!curr && capital > 1) return false;
  }

  return true;
};
