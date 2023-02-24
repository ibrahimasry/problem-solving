class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        res = inf
        mxpq = []
        mn = inf
        for n in nums:
            if n % 2:
                heappush(mxpq,-n*2)
                mn = min(mn, n*2)
            else:
                heappush(mxpq,-n)
                mn = min(mn ,n)

        while mxpq:
            curr = -heappop(mxpq)
            res = min(res , curr - mn)
            if curr % 2 == 1:
                break


            curr //= 2
            mn = min(mn , curr)
            heappush(mxpq,-curr)
        return res
