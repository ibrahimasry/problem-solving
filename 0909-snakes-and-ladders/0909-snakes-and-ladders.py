class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        m = len(board)
        n = len(board[0])
        
        q = deque([1])
        steps = 0
        seen = set()
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == (n * n): return steps
                for pos in range(curr + 1, min(curr + 7, n*n + 1)):
                    r , c = divmod(pos-1,n)
                    nex = board[~r][~c if r % 2 else c]
                    i = pos if nex <= 0 else nex
                    if not (i in seen):
                        q.append(i)
                        seen.add(i)
            steps += 1                
        return -1