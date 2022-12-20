from sortedcontainers import SortedList
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        rainDays = defaultdict(int)
        dryDays = SortedList()
        
        res = []
        
        for day, lake in enumerate(rains):
            if lake == 0:
                res.append(1)
                dryDays.add(day)
            else:
                if lake in rainDays:
                    prev = rainDays[lake]
                    nextDry = bisect.bisect_left(dryDays,prev)
                    if nextDry == len(dryDays):
                        return []
                    nextDryVal = dryDays[nextDry]
                    res[nextDryVal] = lake
                    dryDays.pop(nextDry)
                rainDays[lake] = day
                res.append(-1)
        return res
            