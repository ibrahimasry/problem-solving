class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        ans = 0
        maxNum = 0
        if nums[-1] < n:
            nums += [n]
        for num in nums:
            while num - maxNum > 1:
                if maxNum >= n:
                    return ans
                ans += 1
                maxNum += (maxNum +  1)
            maxNum = maxNum + num

        return ans
                