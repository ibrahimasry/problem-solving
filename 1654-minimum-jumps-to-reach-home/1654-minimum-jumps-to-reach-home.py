class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        q = deque([(0, False)])
        
        seen = set()
        
        seen.add((0, False))
        
        ans = 0
        while q :
            
            for _ in range(len(q)):
                curr, isBack = q.popleft()
                if curr == x:
                    return ans
                nextF = curr + a

                if nextF < 40000 and nextF not in forbidden and (nextF, False) not in seen:
                    q.append((nextF, False))
                    seen.add((nextF, False))

                if not isBack:
                    nextB= curr - b
                    if nextB >= 0 and nextB not in forbidden and (nextB, True) not in seen:
                        q.append((nextB, True))
                        seen.add((nextB, True))
            ans += 1
        forbidden = set(forbidden)
        return -1
