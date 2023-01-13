class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        
        stack = []
        ans= [-1] * len(nums)
        pq = []
        for i, n in enumerate(nums):
            
            while pq and nums[pq[0][1]] < n:
                ans[heapq.heappop(pq)[1]] = n
            while stack and nums[stack[-1]] < n:
                heapq.heappush(pq,(nums[stack[-1]] ,stack.pop()))
            stack.append(i)

                
        return ans