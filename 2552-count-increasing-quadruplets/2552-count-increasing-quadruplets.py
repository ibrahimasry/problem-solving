class Solution:
    def countQuadruplets(self, a: List[int]) -> int:
        res, n = 0, len(a)
        left = [[0 for i in range(n+1)] for j in range(n)]
        right = [[0 for i in range(n+1)] for j in range(n)]
        for i in range(1, n):
            # new array will based on the old array
            left[i] = left[i-1][:]
            # update all the elements greater than a[i-1]
            for j in range(a[i-1] + 1, n + 1):
                left[i][j] += 1
        for i in range(n-2, -1, -1):
            right[i] = right[i+1][:]
            for j in range(a[i+1]):
                right[i][j] += 1
        for j in range(n):
            for k in range(j+1, n):
                # left[j][a[k]] means the count of "until j, < a[k]"
                # right[k][a[j]] means the count of "unitl k, > a[j]"
                if a[j] > a[k]:
                    res += left[j][a[k]] * right[k][a[j]]
        return res
