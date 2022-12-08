class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        freq = Counter(milestones)
        maxProject = max(freq.keys())
        countOfMax = freq[maxProject]
        sumAll = sum(milestones) - countOfMax * maxProject
        if countOfMax == 1:
            if sumAll >= maxProject:
                return sum(milestones)
            return sumAll * 2 + 1
        else :
            return sum(milestones)
        