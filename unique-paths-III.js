// problem link : https://leetcode.com/problems/unique-paths-iii/solution/
// On a 2-dimensional grid, there are 4 types of squares:

//     1 represents the starting square.  There is exactly one starting square.
//     2 represents the ending square.  There is exactly one ending square.
//     0 represents empty squares we can walk over.
//     -1 represents obstacles that we cannot walk over.

// Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

// Example 1:

// Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
// Output: 2
// Explanation: We have the following two paths:
// 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
// 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

const uniquePathsIII = function (grid) {
  let memo = grid.map((row) => row.slice(0).fill(false));
  let start = [0, 0];
  let toVisit = 0;

  for (let i = 0; i < grid.length; i++)
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j] >= 0) toVisit++;
      if (grid[i][j] == 1) {
        start = [i, j];
      }
    }
  return helper(grid, ...start, toVisit, memo);
};

function helper(grid, i, j, toVisit, memo) {
  if (!isValid(grid, i, j, memo)) return 0;
  if (grid[i][j] == 2 && toVisit == 1) return 1;
  memo[i][j] = true;
  const dirs = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
  ];
  let res = 0;

  for (let [x, y] of dirs) {
    let r = x + i;
    let c = y + j;
    res += helper(grid, r, c, toVisit - 1, memo);
  }
  memo[i][j] = false;

  return res;
}

function isValid(grid, i, j, memo) {
  if (
    i < 0 ||
    j < 0 ||
    i >= grid.length ||
    j >= grid[0].length ||
    grid[i][j] == -1 ||
    memo[i][j] == true
  )
    return false;
  return true;
}
