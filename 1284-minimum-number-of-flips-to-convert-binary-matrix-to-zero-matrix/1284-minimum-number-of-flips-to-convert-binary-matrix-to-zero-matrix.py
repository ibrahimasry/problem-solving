class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        r = len(mat)
        c = len(mat[0])
        def better(x,y):
            if x < 0:
                return y
            if y < 0:
                return x
            if y > x: 
                return x
            return x
        def dfs(operations):
            if len(operations) == c:
                change = [0] * c
                last = operations[:]
                maybe = 0
                for row in mat:
                    state = change
                    for j in range(c):
                        state[j] ^= row[j]
                        if last[j] == 1:
                            state[j] ^= 1
                            if j > 0:
                                state[j-1] ^= 1
                            if j + 1 < c:
                                state[j+1] ^= 1
                            maybe += 1
                    change , last = last, state
                for x in last:
                    if x == 1:
                        return -1
                return maybe
            operations.append(0)
            maybe1 = dfs(operations)
            operations[-1] = 1
            maybe2 = dfs(operations)
            operations.pop()
            return better(maybe1,maybe2)
        return dfs([])