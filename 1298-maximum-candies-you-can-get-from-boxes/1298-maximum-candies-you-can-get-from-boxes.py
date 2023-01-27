class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        curr = set(initialBoxes)
        waitToDiscover = set()
        queue = deque(b for b in initialBoxes if status[b] == 1)
        seen = set(queue)
        ans = 0
        while queue:
            box = queue.pop()
            ans += candies[box]
            for b in containedBoxes[box]:
                curr.add(b)
                if (status[b] or b in waitToDiscover) and b not in seen:
                    seen.add(b)
                    queue.append(b)
            for b in keys[box]:
                if b in curr and b not in seen:
                    seen.add(b)
                    queue.append(b)
                else :
                    waitToDiscover.add(b)
        return ans