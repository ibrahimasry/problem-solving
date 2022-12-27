class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        m = len(board)
        n = len(board[0])
        
        q = deque([0])
        steps = 0
        seen = set()
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == (n * n) - 1:
                    return steps

                for pos in range(curr + 1, min(curr + 7, n*n)):
                    r , c = pos // n , pos % n
                    c = (c if r % 2 == 0 else ((n - 1) - c))
                    rVal = (m - r) - 1
                    cVal = c
                    nex = board[rVal][cVal] -1
                    i = pos if nex < 0 else nex
                    if (i in seen) == False:
                        q.append(i)
                        seen.add(i)
            steps += 1                
        return -1