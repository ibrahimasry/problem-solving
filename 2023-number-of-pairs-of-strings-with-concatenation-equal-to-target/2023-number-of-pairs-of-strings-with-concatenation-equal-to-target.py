class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        
        
        hashl = defaultdict(int)
        hashr = defaultdict(int)
        for s in nums:
            l = len(target)
            if target.find(s) >= 0 :
                l = target.index(s)
            r = len(target)
            if target.rfind(s)  >= 0:
                r = target.rindex(s)
            if l == 0:
                hashl[s] += 1
            if r == len(target) - len(s) :
                hashr[s] += 1
        res = 0
        for key in hashl:
            l = key
            r = target[len(key):]
            if l == r:
                res += hashl[key] * (hashl[key] - 1) 
            else :
                res += hashl[key] * hashr[target[len(key):]]
        return res