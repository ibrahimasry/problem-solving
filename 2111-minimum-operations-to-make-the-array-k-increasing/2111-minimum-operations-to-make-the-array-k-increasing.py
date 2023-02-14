class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        res = len(arr)
        for i in range(k):
            dp = []
            for j in range(i,len(arr), k):
                ind = bisect.bisect(dp,arr[j])
                if ind == len(dp):
                    dp.append(arr[j])
                else:
                    dp[ind] = arr[j]
            res -= len(dp)
        return res