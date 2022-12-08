class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        if k % total == 0:
            return 0
        left = (k % total)
        
        for i in range(len(chalk)):
            left -= chalk[i]
            if left < 0:
                return i
