class Solution:
    def isPossible(self, target: List[int]) -> bool:
        
        if len(target) == 1 :
            return target[0] == 1
        total = sum(target)
        currHeap = []
        
        for n in target:
            heapq.heappush(currHeap,-n)
        while -currHeap[0] != 1:
            val = -heapq.heappop(currHeap)
            sub = total - val 
            
            if sub == 1 :
                return True
            remain = val % sub
            if remain == 0 or  val == remain:
                return False
            heapq.heappush(currHeap, -remain)
            total += remain - val
        return True