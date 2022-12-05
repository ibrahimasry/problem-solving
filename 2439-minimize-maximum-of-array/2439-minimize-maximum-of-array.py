class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        
        l = min(nums)
        r = max(nums)  + 1
        
        while l < r :
            m = l + (r-l) // 2
            
            can = True
            if nums[0] > m:
                can = False
            taken = 0
            for i in range(1, len(nums)):
                prev = nums[i-1] + taken
                curr = nums[i]
                
                
                diff = (prev - m)
                
                
                if curr + diff > m:
                    can = False
                    break
                taken = diff
            if  can :
                r = m
            else :
                l = m + 1
        return l
                    
        