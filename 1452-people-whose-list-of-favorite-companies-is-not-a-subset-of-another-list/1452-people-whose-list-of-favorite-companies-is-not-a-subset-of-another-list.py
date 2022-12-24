class Solution:
    def peopleIndexes(self, mat: List[List[str]]) -> List[int]:
        
        m = len(mat)
        for i in range(m):
            mat[i] = set(mat[i])
            
        res = set()
        for i in range(m):
            for j in range(m):
                if i == j:
                    continue
                if mat[i] & mat[j] == mat[j]:
                    res.add(j)
        return sorted(list(set(list(range(m))) - res))
            