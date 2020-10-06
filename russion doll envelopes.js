// 354. Russian Doll Envelopes
// You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

// What is the maximum number of envelopes can you Russian doll? (put one inside other)

// Note:
// Rotation is not allowed.

// Example:

// Input: [[5,4],[6,4],[6,7],[2,3]]
// Output: 3
// Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

/**
 * @param {number[][]} envelopes
 * @return {number}
 */
const maxEnvelopes = function (envelopes) {
  if (envelopes.length == 0) return 0;
  envelopes.sort((a, b) => a[0] - b[0]);

  const dp = Array(envelopes.length).fill(1);
  let max = 1;
  for (let i = 1; i < envelopes.length; i++) {
    for (let j = i - 1; j >= 0; j--) {
      if (
        envelopes[i][1] > envelopes[j][1] &&
        envelopes[i][0] > envelopes[j][0]
      )
        dp[i] = Math.max(dp[i], dp[j] + 1);
    }
    max = Math.max(dp[i], max);
  }
  return max;
};
