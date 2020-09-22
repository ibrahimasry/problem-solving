// problem link  : https://leetcode.com/problems/car-pooling/submissions/
// You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

// Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

// Return true if and only if it is possible to pick up and drop off all passengers for all the given trips.

// Example 1:

// Input: trips = [[2,1,5],[3,3,7]], capacity = 4
// Output: false

// Example 2:

// Input: trips = [[2,1,5],[3,3,7]], capacity = 5
// Output: true
const carPooling = function (trips, capacity) {
  const start = trips.map((a) => a.slice(0, 2)).sort((a, b) => a[1] - b[1]);
  const end = trips.map((a) => [a[0], a[2]]).sort((a, b) => a[1] - b[1]);

  let j = 0;
  let i = 0;
  while (i < trips.length) {
    if (start[i][1] < end[j][1]) {
      if (capacity - start[i][0] < 0) return false;
      capacity -= start[i++][0];
    } else {
      capacity += end[j++][0];
    }
  }
  return true;
};
