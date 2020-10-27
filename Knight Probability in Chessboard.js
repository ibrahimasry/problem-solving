// leetcode 688.Knight Probability in Chessboard
// On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

// A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

// Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

// The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

// Example:

// Input: 3, 2, 0, 0
// Output: 0.0625
// Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
// From each of those positions, there are also two moves that will keep the knight on the board.
// The total probability the knight stays on the board is 0.0625.

/**
 * @param {number} N
 * @param {number} K
 * @param {number} r
 * @param {number} c
 * @return {number}
 */
const knightProbability = function (N, K, r, c) {
  return helper(...arguments, {});
};

function helper(N, K, r, c, cache) {
  if (r < 0 || c < 0 || r >= N || c >= N) return 0;
  if (K == 0) return 1;
  let key = r * N + c + "-" + K;
  if (key in cache) return cache[key];
  const choices = [
    [1, 2],
    [2, 1],
    [1, -2],
    [2, -1],
    [-1, -2],
    [-1, 2],
    [-2, 1],
    [-2, -1],
  ];
  let res = 0;
  for (let [x, y] of choices) {
    res += 0.125 * knightProbability(N, K - 1, r + x, c + y, cache);
  }
  cache[key] = res;
  return res;
}
