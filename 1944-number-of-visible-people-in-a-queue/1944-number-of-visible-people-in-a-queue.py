class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        
        
        stack = []
        res = []
        
        for curr in heights[::-1]:
            size = 0
            while stack and stack[-1] <= curr :
                size += 1
                stack.pop()
            if stack :
                size+=1
            res.append(size)
            stack.append(curr)
        return res[::-1]     
        