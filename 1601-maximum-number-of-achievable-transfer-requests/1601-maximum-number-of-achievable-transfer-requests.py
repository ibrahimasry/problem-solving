class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def helper(mask):
            indegrees = defaultdict(int)
            count = 0
            for i in range(r):
                if  ((1 << i) & mask) :
                    count += 1
                    f , t = requests[i]
                    indegrees[f]  -= 1
                    indegrees[t]   += 1
            for key in indegrees:
                if indegrees[key] != 0:
                    return 0
            return count
        ans = 0
        r = len(requests)
        for i in range(1 << r):
            ans = max(ans, helper(i))
        return ans
        