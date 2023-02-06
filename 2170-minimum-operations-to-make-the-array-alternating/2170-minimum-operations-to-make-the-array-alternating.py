class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        count1 = sorted([(c,v) for v,c in Counter(nums[::2]).items()], reverse=True)
        count2 = sorted([(c,v) for v,c in Counter(nums[1::2]).items()],reverse=True)
        if count1[0][1] != count2[0][1]:
            return len(nums) - (count1[0][0] + count2[0][0])
        res = 0        
        mx1 = count1[0][0]
        mx2 = 0
        if len(count2) > 1:
            mx2 = count2[1][0]
        res = max(mx1+mx2,res)
        
        mx1 = count2[0][0]
        if len(count1) > 1:
            mx2 = count1[1][0]
        res = max(mx1+mx2,res)

        return len(nums) - (res)        
        
