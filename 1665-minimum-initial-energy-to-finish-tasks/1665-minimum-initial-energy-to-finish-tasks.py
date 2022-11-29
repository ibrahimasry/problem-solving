class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:x[1]-x[0], reverse= True)
        def helper(k):
            for a, m in tasks:
                if k < m:
                    return False
                k -= a
            return True

        left = sum([a for a, m in tasks])
        right = sum([m for a, m in tasks]) + 1
        while left < right:
            m = left + (right-left)//2
            if helper(m):
                right = m
            else :
                left = m + 1
        return left
        