class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        n = len(customers)
        
        right = [0] * (n+1)
        
        for i in range(n-1, -1, -1):
            if customers[i] == "Y":
                right[i] += right[i+1] + 1
            else :
                right[i] = right[i+1]
        ans = n 
        curr = 0
        hr = -1
        
        for i, c in enumerate(customers):
            if right[i] + curr < ans:
                ans = right[i] + curr
                hr = i
            
            if c == "N":
                curr += 1
        if curr + right[-1] < ans :
            return n
        return hr
            
        