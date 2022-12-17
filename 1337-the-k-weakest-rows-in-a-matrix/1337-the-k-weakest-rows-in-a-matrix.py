class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        n = len(mat[0])
        m = len(mat)
        
        arr = []
        res = []
        
        for i in range(m):
            count = 0
            for j in range(n):
                if mat[i][j] :
                    count += 1
                else :
                    break
            arr.append((count,i))
        return [x for c , x in sorted(arr)[:k]]