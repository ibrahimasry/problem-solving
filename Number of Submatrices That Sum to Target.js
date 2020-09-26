// problem link : https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
// 1074. Number of Submatrices That Sum to Target
// Hard
// Given a matrix and a target, return the number of non-empty submatrices that sum to target.

// A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

// Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

// Example 1:

// Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
// Output: 4
// Explanation: The four 1x1 submatrices that only contain 0.
// Example 2:

// Input: matrix = [[1,-1],[-1,1]], target = 0
// Output: 5
// Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
// Example 3:

// Input: matrix = [[904]], target = 0
// Output: 0

var numSubmatrixSumTarget = function (matrix, target) {
  let cols = matrix[0].length;
  let rows = matrix.length;
  // get  prefix sum for every row
  for (let i = 0; i < rows; i++) {
    for (let j = 1; j < cols; j++) {
      matrix[i][j] += matrix[i][j - 1];
    }
  }

  let res = 0;
  //loop over every adjacent columns and sum the prefix sum that we already have from the previous loop
  for (let startCol = 0; startCol < cols; startCol++) {
    for (let endCol = startCol; endCol < cols; endCol++) {
      let counter = { 0: 1 };
      // the sum of the curr submatrix
      let curr = 0;
      // loop over all row  between those cols
      for (let startRow = 0; startRow < rows; startRow++) {
        //get the sum of the curr sub array and sum it with the above submatrix
        curr +=
          matrix[startRow][endCol] -
          (startCol == 0 ? 0 : matrix[startRow][startCol - 1]);
        // if we have prefix sum with that diff , so we have submatrix with target sum yaay
        res +=
          counter[curr - target] !== undefined ? counter[curr - target] : 0;
        // store the curr submatrix sum till that row
        counter[curr] = counter[curr] !== undefined ? ++counter[curr] : 1;
      }
    }
  }
  return res;
};
