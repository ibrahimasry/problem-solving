class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        
        diff = defaultdict(int)
        summ = defaultdict(int)
        
        for n in range(len(nums)//2):
            
            
            left = nums[n]
            right = nums[len(nums)-n-1]
            
            minn = min(left, right)
            maxn = max(left, right)
            diff[minn+1] -= 1
            diff[maxn+limit+1] += 1
            summ[left+right] += 1
        curr = len(nums)
        ans = curr
        for i in range(2, max(summ)+1):
            curr += diff[i]
            ans = min(ans, curr - summ[i])
        return ans