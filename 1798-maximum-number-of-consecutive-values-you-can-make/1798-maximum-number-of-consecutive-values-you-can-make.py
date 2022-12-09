class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        
        can = 0
        for i in coins:
            if i - can > 1:
                return can + 1
            can += i
        return can + 1