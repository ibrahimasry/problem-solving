class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        res = []
        
        i = 2
        if finalSum % 2:
            return []
        while finalSum - i >= 0 :
                finalSum -= i
                res.append(i)
                i += 2

        if finalSum:
            res[-1] += finalSum

        return res