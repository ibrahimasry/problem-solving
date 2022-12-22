class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        pos = [n for n in nums if n > 0]
        neg = sorted([abs(n) for n in nums if n < 0])
        zeros = sum([1 for n in nums if n == 0])
        posTotal = sum(pos)
        negTotal = sum(neg)
        
        
        if len(neg) == 0 and zeros:
            return posTotal
        if len(neg) == 0 :
            if k%2:
                return posTotal - 2 * min(nums)
            else:
                return posTotal
        if len(neg) == k:
            return posTotal + negTotal
        if len(neg) < k and zeros:
            return negTotal + posTotal
        if len(neg) < k :
            if (len(neg)  - k) % 2 == 0:
                return sum(pos) + sum(neg) 
            return sum(pos) + sum(neg) - 2 * min(min(pos + [1001]) , min(neg + [1001]))
        if len(neg) > k:
            return sum(pos) + sum(neg) - 2 * sum(neg[:-k])
        
        
        
        