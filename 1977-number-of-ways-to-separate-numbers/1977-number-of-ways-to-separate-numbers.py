class Solution:
    def numberOfCombinations(self, num: str) -> int:
        n = len(num)
        prefix = [[0] * (n+1) for _ in range(n+1)]
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
                        if num[j-l:j] <= num[j:i + 1]:
                            curr = prefix[j-1][l]
                        else:
                            curr = prefix[j-1][l-1]
                prefix[i][l] += prefix[i][l-1] + curr            
        return prefix[n-1][n]  % (10 ** 9 + 7 )              
                    