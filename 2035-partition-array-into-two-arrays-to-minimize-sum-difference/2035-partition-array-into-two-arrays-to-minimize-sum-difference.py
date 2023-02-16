from sortedcontainers import SortedSet
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        s = sum(nums) 
        half = sum(nums) // 2
        n = len(nums)//2
        
        res = inf
        for i in range(n+1):
            left = [sum(com) for com in combinations(nums[:n],i)]
            right = sorted([sum(com) for com in combinations(nums[n:], n - i)])
            for a in left:
                b = half - a
                curr = bisect.bisect_left(right,b)
                if curr > 0:
                    cand2 = right[curr-1]
                    l = cand2 + a
                    r = s - l
                    if abs(l-r) < res:
                        res = abs(l-r)
                if curr < len(right):
                    cand2 = right[curr]
                    l = cand2 + a
                    r = s - l
                    if abs(l-r) < res:
                        res = abs(l-r)
        return res
