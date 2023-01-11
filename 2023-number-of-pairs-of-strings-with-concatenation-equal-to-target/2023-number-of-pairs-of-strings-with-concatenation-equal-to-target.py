class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        
        freq = Counter(nums)
        res = 0
        for key in freq:
            if target[:len(key)] != key: continue
            l = key
            r = target[len(key):]
            if l == r:
                res += freq[key] * (freq[key] - 1) 
            else :
                res += freq[key] * freq[r]
        return res