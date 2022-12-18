class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        
        ans = set()
        prev = nums.index(key)
        for i , v in enumerate(nums):
            if v == key:
                prev=i
            if abs(i-prev) <= k:
                ans.add(i)
        
        
        for i in range(len(nums)-1,-1,-1):
            v = nums[i]
            if v == key:
                prev=i
            if abs(i-prev) <= k:
                ans.add(i)

            
        return sorted(list(ans))