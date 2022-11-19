class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        
        
        
        
        
        @lru_cache(None)
        def dp(remain, groups):
            if not groups:
                return 0
            ans = 0
            
            for i in range(len(groups)) :
                newRemain =  (remain + groups[i]) % batchSize
                ans = max(ans, (remain == 0) + dp(newRemain, tuple(groups[:i]+groups[i+1:])))
            return ans
        n = len(groups)
        groups = [num % batchSize for num in groups if num % batchSize]
        
        ans = n - len(groups)
        freq = Counter(groups)
        
        for num in range(1, batchSize):
            matchNum = batchSize - num
            match = 0
            if matchNum == num:
                match = freq[num] // 2
            else:
                match = min(freq[matchNum], freq[num])
            ans += match
            freq[matchNum] -= match
            freq[num] -= match
        newGroup = []
        
        for num, count in freq.items():
            newGroup += [num] * count
        n = len(newGroup)
        return ans + dp(0, tuple(newGroup))
        