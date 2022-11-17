class Solution:
    def racecar(self, target: int) -> int:
        
        seen = set()
        seen.add((0,1))
        queue = deque()
        queue.append((0,1))
        
        steps = 0
        while queue:
            for _ in range(len(queue)):
                pos, speed = queue.popleft()
                newPos = pos + speed
                if newPos == target:
                    return steps + 1
                newSpeed = 2 * speed
                
                if abs(newSpeed) < 2 * target and abs(newPos) < 2 * target and (newPos, newSpeed) not in seen:
                    queue.append((newPos, newSpeed))
                    seen.add((newPos, newSpeed))
                newSpeed = -1 if speed > 0 else 1
                if (pos, newSpeed) not in seen:
                    queue.append((pos, newSpeed))
                    seen.add((pos, newSpeed))
            steps += 1
        