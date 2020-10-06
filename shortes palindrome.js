// leetcode 214. Shortest Palindrome
// Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

// Example 1:

// Input: "aacecaaa"
// Output: "aaacecaaa"
// Example 2:

// Input: "abcd"
// Output: "dcbabcd"

const shortestPalindrome = function (s) {
  const rev = s.split("").reverse().join("");

  const newStr = s + "#" + rev;

  const table = new Array(newStr.length).fill(-1);

  let j = 0;
  let i = 1;

  while (i < newStr.length) {
    if (newStr[i] == newStr[j]) {
      table[i++] = j++;
    } else {
      if (j > 0) j = table[j - 1] + 1;
      else i++;
    }
  }

  return rev.slice(0, s.length - table[table.length - 1] - 1) + s;
};
