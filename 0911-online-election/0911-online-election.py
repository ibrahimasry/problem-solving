class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leaders = []
        self.count = defaultdict(int)
        leader= 0
        maxTotal = 0
        leaders = self.leaders
        count = self.count
        for p, t in zip(persons, times):
            count[p] += 1
            if count[p] >= maxTotal:
                leader = p
                maxTotal = count[p]
                leaders.append((t,leader))

    def q(self, t: int) -> int:
        
        idx = bisect.bisect(self.leaders, (t,inf)) - 1
        return self.leaders[idx][1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)