class Solution:
    def __init__(self):
        self.n = -1

    def sum_on_row(self, r: List[int]) -> int:
        l = [-1]
        su = 0

        for i in range(self.n):
            while len(l) > 1 and r[i] <= r[l[-1]]:
                k = l.pop()
                su += r[k] * (k - l[-1]) * (i - k)
            l.append(i)
        while len(l) > 1:
            k = l.pop()
            su += r[k] * (k - l[-1]) * (self.n - k)

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
