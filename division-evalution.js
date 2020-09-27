// 399. Evaluate Division
// You are given equations in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating-point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

// The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

// Example 1:

// Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
// Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
// Explanation:
// Given: a / b = 2.0, b / c = 3.0
// queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
// return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

// solution by union find
const calcEquation = function (equations, values, queries) {
  const chars = {};
  const dist = {};
  for (let i = 0; i < equations.length; i++) {
    let [x, y] = equations[i];

    union(x, y, chars, dist, values[i]);
  }

  for (let i = 0; i < queries.length; i++) {
    let [x, y] = queries[i];
    if (chars[x] == undefined || chars[y] == undefined) {
      queries[i] = -1;
      continue;
    }

    const xParent = find(x, chars, dist);
    const yParent = find(y, chars, dist);
    //if the two variables dont sare the same parent we cant solve the query
    if (xParent !== yParent) queries[i] = -1;
    // else divide each distance from the shared root
    // a ==> b  , c ===> b    , a / c = (a / b) * (b / c) == (a / b)  / (c / b)
    else queries[i] = dist[x] / dist[y];
  }

  return queries;
};

function find(x, chars, dist) {
  if (chars[x] == undefined) {
    chars[x] = x;
    dist[x] = 1;
    return x;
  }
  if (chars[x] == x) return x;
  let lastP = chars[x];
  chars[x] = find(chars[x], chars, dist);
  // the distance from the curr var to the root is the distance of
  // its last parent to the root * the x distnce to  the last parent
  dist[x] = dist[lastP] * dist[x];
  return chars[x];
}

function union(x, y, chars, dist, value) {
  const xParent = find(x, chars, dist);
  const yParent = find(y, chars, dist);
  chars[xParent] = yParent;
  dist[xParent] = (dist[y] * value) / dist[x];
}
