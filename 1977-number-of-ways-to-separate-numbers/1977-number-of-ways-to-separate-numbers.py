class Solution:
    def numberOfCombinations(self, num: str) -> int:
        n = len(num)
        prefix = [[0] * (n+1) for _ in range(n+1)]
        lcs = [[0] * (n + 1) for _ in range(n)]
        
        
        for i in range(n-2, -1, -1):
            for j in range(i+1, n) :
                if num[i] == num[j]:
                    lcs[i][j] = lcs[i+1][j+1] + 1
        for i in range(n):
            for l in range(1, i+2):
                j = i - l + 1
                curr = 0
                if num[j] == "0" :
                    curr = 0
                elif j == 0 :
                    curr = 1
                elif j < l :
                    curr = prefix[j-1][j]
                else :
                    nextL = lcs[j-l][j]
                    if nextL >= l or num[j-l+nextL] < num[j+nextL] :
                        curr = prefix[j-1][l]
                    else:
                        curr = prefix[j-1][l-1]
                prefix[i][l] += prefix[i][l-1] + curr            
        return prefix[n-1][n]  % (10 ** 9 + 7 )              
                    