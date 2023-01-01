class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(time):
            return int(time[:2]) * 60 + int(time[3:])
        
        
        times = list(map(convert, timePoints))
        times.sort()
        return min((curr-prev + (60 * 24)) % (60 * 24) for prev, curr in zip(times, times[1:] + times[:1]))