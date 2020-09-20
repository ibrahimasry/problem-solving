// problem link https://leetcode.com/problems/sequential-digits/
// An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

// Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

// Example 1:

// Input: low = 100, high = 300
// Output: [123,234]

//solution with bfs
const sequentialDigits = function (low, high) {
  if (low == high) return [];
  const queue = _.range(1, 10);
  const res = [];
  while (queue.length) {
    const curr = queue.shift();
    if (curr > high) break;
    if (curr >= low) res.push(curr);
    let tens = curr % 10;
    if (tens < 9) queue.push(curr * 10 + ++tens);
  }
  return res;
};
