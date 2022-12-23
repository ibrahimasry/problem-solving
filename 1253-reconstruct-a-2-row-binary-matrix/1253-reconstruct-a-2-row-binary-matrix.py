class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        A = [[0] * len(colsum) for _ in range(2)]
        

        for j in range(len(colsum)):
            if  colsum[j] == 2 :
                A[0][j] = A[1][j] = 1
                upper -= 1
                lower -= 1
                colsum[j] -= 2
            elif colsum[j] == 1:
                if upper > lower :
                    A[0][j] = 1
                    upper -= 1
                    colsum[j] -= 1

                else:
                    A[1][j] = 1
                    lower -= 1
                    colsum[j] -= 1
        return [] if lower != upper or lower != 0 else A