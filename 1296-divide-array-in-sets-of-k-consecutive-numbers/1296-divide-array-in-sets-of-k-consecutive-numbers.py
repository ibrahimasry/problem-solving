class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False
        count = Counter(nums)
        start = deque()
        last = -1
        open = 0
        
        for n in sorted(count):
            if count[n] < open or open > 0 and last + 1 != n:
                return False
            start.append(count[n] - open)
            open = count[n]
            last = n
            if len(start) == k :
                open -= start.popleft()
        return open == 0