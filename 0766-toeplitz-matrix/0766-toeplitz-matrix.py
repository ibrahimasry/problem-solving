class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        hash = defaultdict(set)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                hash[i-j].add(matrix[i][j])
        for distinct in hash.values():
            if len(distinct) != 1:
                return False
        return True