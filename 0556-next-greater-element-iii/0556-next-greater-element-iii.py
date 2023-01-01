class Solution:
    def nextGreaterElement(self, n: int) -> int:
        prev = -1
        
        n = list(str(n))
        l = len(n)
        
        i = l - 1
        while i > 0 and n[i] <= n[i-1]:
            i -= 1
        if i == 0:
            return -1
        i -= 1
        j = l - 1
        while j > i and n[j] <= n[i]:
            j -= 1
        n[j] , n[i] = n[i] , n[j]
        
        n[i+1:] = reversed(n[i+1:])
        return -1 if int("".join(n)) > 2 ** 31 -1 else int("".join(n)) 