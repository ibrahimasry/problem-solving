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
                    nextDry = bisect.bisect_left(dryDays,rainDays[lake])
                    if nextDry == len(dryDays):
                        return []
                    res[dryDays[nextDry]] = lake
                    dryDays.pop(nextDry)
                rainDays[lake] = day
                res.append(-1)
        return res
            