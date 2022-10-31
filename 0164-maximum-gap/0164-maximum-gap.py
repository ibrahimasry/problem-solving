class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2 :
            return 0
        nmax = max(nums)
        nmin = min(nums)
        diff = nmax - nmin
        if diff == 0 :
            return 0
        n = len(nums)
        bucketSize = max(diff // (n-1), 1)
        buckets = defaultdict(list)

        for num in nums:
            bucket = (num - nmin) // bucketSize
            if not buckets[bucket]:
                buckets[bucket] = [num, num]
                continue
            buckets[bucket][1] = max(buckets[bucket][1], num)
            buckets[bucket][0] = min(buckets[bucket][0], num)
        ans = 0
        pre = -1
        for i in sorted(buckets.keys()):
            if pre != -1:
                ans = max(ans, buckets[i][0] - pre)
            pre = buckets[i][1]
        return ans
        
