/**
 * @param {number[]} nums
 * @return {number}
 */
var countQuadruplets = function(nums) {
    const n = nums.length
    const dp = Array(n).fill(0)
    let ans = 0
    for (let i = 0; i < n; i++)
        {
            let prev = 0
            for (let j = 0; j < i; j++){
                if (nums[j] > nums[i])
                    dp[j] += prev
                else {
                    ans += dp[j]
                    prev += 1
                }
                
            }
        }
    return ans
};