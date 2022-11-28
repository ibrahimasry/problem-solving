class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        
        
        
        counts = []
        
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            zero = 0
            for j in range(m-1, -1, -1):
                if grid[i][j] == 1 :
                    break
                else:
                    zero += 1
            counts.append(zero)
        res = 0
        for i  in range(m-1):
            count = counts[i]
            req = max(m - i - 1, 0)
            swapIndex = i 
            while swapIndex < n and counts[swapIndex] < req:
                swapIndex +=1
            if swapIndex == n:
                return -1
            res += abs(i-swapIndex)
            while swapIndex > i:
                counts[swapIndex] , counts[swapIndex - 1] = counts[swapIndex-1] , counts[swapIndex]
                swapIndex -= 1
                
        return res
            
        