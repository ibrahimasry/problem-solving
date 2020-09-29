const numSubarrayProductLessThanK = function (nums, k) {
  if (k == 0) return 0;
  let res = 0;
  let curr = 1;
  let left = 0;
  for (let right = 0; right < nums.length; right++) {
    curr *= nums[left];
    while (curr >= k && left <= right) {
      curr /= nums[left++];
    }
    if (curr < k) res += right - left + 1;
  }

  return res;
};
