class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counter = Counter()
        counter[0] = 1
        
        res = 0
        curr = 0
        for n in nums:
            
            curr += n 
            if counter[curr % k] > 0:
                res += counter[curr%k]
            counter[curr%k] += 1
        return res
                