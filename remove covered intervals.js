// 1288. Remove Covered Intervals
// Given a list of intervals, remove all intervals that are covered by another interval in the list.

// Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

// After doing so, return the number of remaining intervals.

// Example 1:

// Input: intervals = [[1,4],[3,6],[2,8]]
// Output: 2
// Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
// Example 2:

// Input: intervals = [[1,4],[2,3]]
// Output: 1
// Example 3:

// Input: intervals = [[0,10],[5,12]]
// Output: 2
// Example 4:

// Input: intervals = [[3,10],[4,10],[5,11]]
// Output: 2
// Example 5:

// Input: intervals = [[1,2],[1,4],[3,4]]
// Output: 1

const removeCoveredIntervals = function (intervals) {
  intervals.sort((a, b) => (a[0] - b[0] == 0 ? b[1] - a[1] : a[0] - b[0]));

  let prev = intervals[0];
  let res = 0;
  for (let i = 1; i < intervals.length; i++) {
    let curr = intervals[i];

    if (curr[0] <= prev[1] && curr[1] <= prev[1]) {
      res++;
      if (curr[1] >= prev[1]) prev = curr;
    } else prev = curr;
  }

  return intervals.length - res;
};
