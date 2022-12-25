class Solution:
    def answerQueries(self, nums: List[int], q: List[int]) -> List[int]:
        nums.sort()
        q = [[v,i] for i, v in enumerate(q)]
        q.sort()
        ans = [0] * len(q)
        
        curr = 0
        i = 0
        j = 0
        while i < len(q) :
            while j < len(nums)  and q[i][0] >= curr + nums[j]:
                curr += nums[j]

                j += 1
            ans[q[i][1]] = j 
            i += 1
        return ans