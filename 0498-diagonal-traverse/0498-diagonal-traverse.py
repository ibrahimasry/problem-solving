class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        hash = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                hash[i+j].append(mat[i][j])
        ans = []
        for key in (hash):
            if key % 2:
                ans += hash[key]
            else :
                ans += reversed(hash[key])
        return ans