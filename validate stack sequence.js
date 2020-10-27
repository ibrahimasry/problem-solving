// leetcode 946. Validate Stack Sequences

// Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

// Example 1:

// Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
// Output: true
// Explanation: We might do the following sequence:
// push(1), push(2), push(3), push(4), pop() -> 4,
// push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
// Example 2:

// Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
// Output: false
// Explanation: 1 cannot be popped before 2.

const validateStackSequences = function (pushed, popped) {
  const curr = [];
  let i = 0;
  let j = 0;
  while (j < pushed.length) {
    while (
      j < pushed.length &&
      (curr.length == 0 || popped[i] !== curr[curr.length - 1])
    )
      curr.push(pushed[j++]);
    while (i < popped.length && popped[i] == curr[curr.length - 1]) {
      curr.pop();
      i++;
    }
  }

  return pushed.length == i && popped.length == j;
};
