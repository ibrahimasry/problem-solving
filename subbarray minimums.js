// leetcode 907. Sum of Subarray Minimums
// Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

// Since the answer may be large, return the answer modulo 10^9 + 7.

 

// Example 1:

// Input: [3,1,2,4]
// Output: 17
// Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
// Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
 

// Note:

// 1 <= A.length <= 30000
// 1 <= A[i] <= 30000
 




const last = (arr) => arr[arr.length - 1];
const empty = (arr) => arr.length === 0;
const len = (arr) => arr.length;
const enumerate = (arr) => arr.map((a, i) => [i, a]);
const sumSubarrayMins = function (A) {
  let stack = [];
  let sum = 0;
  const mod = 1e9 + 7;
  const left = [];
  for (let [i, curr] of enumerate(A)) {
    while (!empty(stack) && A[last(stack)] >= curr) {
      stack.pop();
    }
    left[i] = !empty(stack) ? i - last(stack) : i + 1;
    stack.push(i);
  }
  stack = [];
  const right = [];
  for (let [i, curr] of enumerate(A).reverse()) {
    while (!empty(stack) && A[last(stack)] > curr) {
      stack.pop();
    }
    right.push(!empty(stack) ? last(stack) - i : len(A) - i);
    stack.push(i);
  }
  right.reverse();
  for (let i = 0; i < len(A); i++)
    sum = (sum + left[i] * right[i] * A[i]) % mod;
  return sum;
};

/**
 * @param {number[]} A
 * @return {number}
 */
const sumSubarrayMins2 = function (A) {
  let left = [];
  let leftMin = [];
  for (let i = 0; i < A.length; i++) {
    let curr = A[i];
    let index = i;
    while (left.length !== 0 && curr <= A[last(left)]) index = left.pop();
    leftMin[i] = leftMin[index] !== undefined ? leftMin[index] : index;
    left.push(i);
  }

  let right = [];
  let rightMin = [];
  for (let i = A.length - 1; i >= 0; i--) {
    let curr = A[i];
    let index = i;
    while (right.length !== 0 && curr < A[last(right))
      index = right.pop();
    rightMin[i] = rightMin[index] !== undefined ? rightMin[index] : index;
    right.push(i);
  }
  let res = 0;
  for (let i = 0; i < A.length; i++) {
    res +=
      ((i - leftMin[i] + 1) * (rightMin[i] - i + 1) * A[i]) % (10 ** 9 + 7);
  }

  return res % (10 ** 9 + 7);
};
