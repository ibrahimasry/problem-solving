class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        
        i = k 
        j = k
        n = len(nums)
        maxn = min(nums) * n
        minn = nums[k]
        while i > 0 or j < n -1:
            
            if i > 0 and j < n-1:
                if nums[i-1] < nums[j+1]:
                    j += 1
                    minn = min(minn, nums[j])
                else :
                    i -= 1
                    minn = min(minn, nums[i])

            elif i > 0:
                i -= 1
                minn = min(minn, nums[i])

            else:
                j += 1
                minn = min(minn, nums[j])
            maxn = max(maxn, minn * (j-i+1))
        return maxn

                
        