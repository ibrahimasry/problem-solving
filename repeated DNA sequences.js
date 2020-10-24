// leetcode 187. Repeated DNA Sequences

// All DNA is composed of a series of nucleotides abbreviated as
// 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When
// studying DNA, it is sometimes useful to identify repeated
// sequences within the DNA.

// Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

// Example 1:

// Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
// Output: ["AAAAACCCCC","CCCCCAAAAA"]

/**
 * @param {string} s
 * @return {string[]}
 */
var findRepeatedDnaSequences = function (s) {
  const map = { A: 0, C: 1, G: 2, T: 3 };
  let base = 4 ** 9;
  let currWindow = 0;
  const hash = new Set();
  for (let i = 0; i < 10; i++) {
    currWindow = currWindow * 4 + map[s[i]];
  }

  const set = new Set();
  hash.add(currWindow);
  for (let i = 10; i < s.length; i++) {
    currWindow -= base * map[s[i - 10]];
    currWindow = currWindow * 4 + map[s[i]];
    if (hash.has(currWindow)) {
      set.add(s.slice(i - 9, i + 1));
    } else hash.add(currWindow);
  }

  return [...set];
};
