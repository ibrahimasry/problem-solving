class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        total = 0
        def dfs(nums):
            nonlocal total
            if len(nums) < 2:
                return nums
            left = dfs(nums[:len(nums)//2])
            right = dfs(nums[len(nums)//2:])
            
            res = []
            t = 0
            i = 0
            while i < len(left):
                t += bisect.bisect(right,(left[i]-1)//2)
                i+=1
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else :
                    res.append(right[j])
                    j+=1
            while i < len(left):
                res.append(left[i])
                i+=1
            while j < len(right):
                res.append(right[j])
                j += 1
            total += t
            return res
        dfs(nums)
        return total
                