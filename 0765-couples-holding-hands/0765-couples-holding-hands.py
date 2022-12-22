class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        
        n = len(row)
        
        pairs = {v:k for k, v in enumerate(row)}
        
        count = 0
        for i in range(0,n,2):
            couple = row[i]-1 if row[i] % 2 else row[i] + 1 
            coupleIdx = pairs[couple]
            if coupleIdx != i + 1:
                temp = pairs[couple]
                pairs[couple] = i+1
                pairs[row[i+1]] = temp
                row[temp] = row[i+1]
                count += 1
        return count