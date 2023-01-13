class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        if len(num) < 3:
            return False
        def dfs(i , seq , ids):
            if i + len(seq) >= n :
                if ids == "f":
                    return False
                return True
            for j in range(i+1,n+1):
                if num[i] == "0" and j != i+1:
                    return False
                if num[j:].startswith(str(int(num[i:j]) + int(seq))):
                    if str(int(num[i:j]) + int(seq)) == num[j:]:
                        return True
                    if dfs(j, num[i:j] , 's'):
                        return True
            return False
        n = len(num)
        for i in range(1, n):
            if num[0] == "0" and  i > 1:
                    return False

            if  dfs(i, num[:i] , 'f'):
                return True
        return False