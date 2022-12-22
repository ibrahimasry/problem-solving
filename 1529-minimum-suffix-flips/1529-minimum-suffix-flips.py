class Solution:
    def minFlips(self, target: str) -> int:
        count = 0
        
        for c in target:
            if int(c) != count % 2:
                count += 1
        return count