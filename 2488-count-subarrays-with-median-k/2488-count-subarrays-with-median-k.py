class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pivot = nums.index(k)
        right = Counter()
        right[0] = 1
        summ = 0
        for i in range(pivot+1, len(nums)):
            n = nums[i]
            summ += (1 if n > k else -1)
            right[summ] += 1
        
        left = Counter()
        
        left[0] = 1
        summ = 0
        for i in range(pivot-1, -1, -1):
            n = nums[i]
            summ += (1 if n > k else -1)
            left[summ] += 1
            
        ans = 0
        for val , count in left.items():
            ans += count * right[-val]
            ans += count * right[1-val]

        return ans