class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        hash = defaultdict(list)
        
        n = len(mat[0])
        m = len(mat)
        
        for i in range(m):
            for j in range(n):
                hash[j-i].append(mat[i][j])
        for k, v in hash.items():
            hash[k].sort(reverse=True)
        for i in range(m):
            for j in range(n):
                mat[i][j] = hash[j-i].pop()
        return mat