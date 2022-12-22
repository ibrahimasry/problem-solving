class Solution:
    def minFlips(self, target: str) -> int:
        count = 0
        
        for i, c in enumerate(target):
            if int(c) != count % 2:
                count += 1
        return count