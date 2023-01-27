class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        discovered = set(initialBoxes)
        queue = deque(b for b in initialBoxes if status[b] == 1)
        ans = 0
        while queue:
            box = queue.pop()
            ans += candies[box]
            for b in containedBoxes[box]:
                discovered.add(b)
                if (status[b]) :
                    queue.append(b)
            for b in keys[box]:
                if b in discovered and status[b] == 0:
                    queue.append(b)
                status[b] = 1
        return ans