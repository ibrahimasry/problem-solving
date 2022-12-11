class Solution:
    def __init__(self):
        self.n = -1

    def sum_on_row(self, r: List[int]) -> int:
        l = [-1]
        su = 0

        for i in range(self.n + 1):
            while (len(l) > 1 and (i == self.n  or r[i] <= r[l[-1]] )):
                k = l.pop()
                su += r[k] * (k - l[-1]) * (i - k)
            l.append(i)

        return su

    def numSubmat(self, mat: List[List[int]]) -> int:
        self.n = len(mat[0])
        r = [0] * self.n
        su = 0
        for row in mat:
            for i in range(self.n):
                r[i] = r[i] + 1 if row[i] == 1 else 0
            su += self.sum_on_row(r)
        return su
