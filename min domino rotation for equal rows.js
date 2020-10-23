// leetcode 1007. Minimum Domino Rotations For Equal Row

// In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

// We may rotate the ith domino, so that A[i] and B[i] swap values.

// Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

// If it cannot be done, return -1.

/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number}
 */

const minDominoRotations = function (A, B) {
  let countA = Array(7).fill(0);
  let countB = Array(7).fill(0);
  let same = Array(7).fill(0);

  for (let i = 0; i < A.length; i++) {
    countA[A[i]] = countA[A[i]] ? ++countA[A[i]] : 1;
    countB[B[i]] = countB[B[i]] ? ++countB[B[i]] : 1;
    if (A[i] == B[i]) same[B[i]] = same[B[i]] ? ++same[B[i]] : 1;
  }

  for (let i = 1; i <= 7; i++) {
    if (countB[i] + countA[i] - same[i] == A.length)
      return Math.min(countB[i], countA[i]) - same[i];
  }
  return -1;
};
// another solution to think about how the above one work
const minDominoRotations2 = function (A, B) {
  let countA = {};
  for (let n of A) {
    countA[n] = countA[n] ? ++countA[n] : 1;
    if (countA[n] >= A.length) return 0;
  }

  let countB = {};
  for (let n of B) {
    countB[n] = countB[n] ? ++countB[n] : 1;
    if (countB[n] >= A.length) return 0;
  }
  let res = 0;
  for (let i = 0; i < A.length; i++) {
    let a = A[i],
      b = B[i];
    //if it's the same dont swap
    if (a == b) continue;
    // if count of b in the upper row is >= tha half and count of b in the upper row is > count of b in the lower so we swap it and the sma elogic for the lower row
    if (
      (countA[b] >= A.length / 2 && countA[b] > countB[b]) ||
      (countB[a] >= A.length / 2 && countB[a] > countA[a])
    ) {
      countA[b]++;
      countB[a]++;
      countA[a]--;
      countB[b]--;
      res++;
    }
    if (countA[b] >= A.length || countB[a] >= A.length) return res;
  }

  return -1;
};
