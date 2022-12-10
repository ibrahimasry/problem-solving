class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        
        n = len(nums)
    
    
        queue = deque([0])
        for i in range(1, n):
            if i - queue[0] > k:
                queue.popleft()
            if queue:
                nums[i] +=  nums[queue[0]]
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
        return nums[-1]