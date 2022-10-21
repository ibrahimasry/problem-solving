class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        
        def getNearest(arr):
            sortedSum = [0]
            currSum = 0
            ans = -sys.maxsize
            for num in arr :
                currSum += num
                if currSum == k :
                    return k
                index = bisect_left(sortedSum, (currSum - k ))
                if index < len(sortedSum):
                    ans = max(ans, currSum - sortedSum[index])
                if ans == k :
                    break
                bisect.insort(sortedSum, currSum )
            return ans
        presum = []
        
        n = len(matrix)
        m = len(matrix[0])
        
        for r in range(n):
            row = []
            for c in range(m):
                if c == 0:
                    row.append(matrix[r][c])
                else:
                    row.append(matrix[r][c] + row[-1])
            presum.append(row)
        ans = -sys.maxsize
        for c1 in range(m):
            for c2 in range(c1+1):
                totalRec = []
                for r in range(n):

                    currSum = presum[r][c1] - (presum[r][c2-1] if c2 > 0 else 0)
                    totalRec.append(currSum)
                currRes =  getNearest(totalRec)
                if k == currRes:
                    return k
                ans = max(ans, currRes)
        return ans