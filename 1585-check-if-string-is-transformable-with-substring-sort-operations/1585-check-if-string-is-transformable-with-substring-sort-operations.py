class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        
        index = [deque() for _ in range(10)]
        
        for i, v in enumerate(s):
            index[int(v)].append(i)
        for i, curr in enumerate(t):
            val = int(curr)
            if not index[val]:
                return False
            for j in range(val):
                if index[j] and  index[j][0] < index[val][0] :
                    return False
            index[val].popleft()
        return True
        