class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        m = len(board)
        n = len(board[0])
        
        q = deque([0])
        need = {0:0}
        steps = 0
        seen = set()
        seen.add(0)
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == (n * n) - 1:
                    return need[curr] 

                for pos in range(curr + 1, curr + 7):
                    if pos in seen or pos >= n*n:
                        continue
                    r , c = pos // n , pos % n
                    c = (c if r % 2 == 0 else ((n - 1) - c))
                    rVal = (m - r) - 1
                    cVal = c

                    nex = pos if board[rVal][cVal] <= 0 else board[rVal][cVal] - 1
                    if nex not in need:
                        need[nex] = need[curr] + 1
                        q.append(nex)
        return -1