// Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

// Integers in each row are sorted from left to right.
// The first integer of each row is greater than the last integer of the previous row.

const searchMatrix = function (matrix, target) {
  if (matrix.length == 0) return false;
  let col = matrix[0].length - 1;
  let row = 0;

  while (col >= 0 && row < matrix.length) {
    if (matrix[row][col] == target) return true;
    if (matrix[row][col] > target) col--;
    else row++;
  }

  return false;
};
