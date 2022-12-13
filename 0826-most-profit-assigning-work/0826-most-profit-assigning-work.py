class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        profit = [(v, i) for i, v in enumerate(profit)]
        worker.sort(reverse=True)
        profit.sort(reverse=True)
        
        
        p = 0
        w = 0
        res = 0
        n= len(profit)
        m = len(worker)
        while p < n and w < m:
            if difficulty[profit[p][1]] <= worker[w]:
                res += profit[p][0]
                w += 1
            else :
                p += 1
        return res