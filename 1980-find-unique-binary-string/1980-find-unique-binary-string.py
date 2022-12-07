class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        
        seen = set(nums)
        def dfs(i, curr):
            if i == len(nums[0]):
                if curr not in seen:
                    return curr
                else :
                    return ''
            
            res = dfs(i+1, curr + "0")
            if res != "" :
                return res
            else:
                return dfs(i+1, curr + "1")
        return dfs(0, '')