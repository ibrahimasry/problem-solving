class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        
        
        strCnt = s.count(letter)
        stackCnt = 0
        stack = []
        
        
        for i, c in enumerate(s) :
            while stack and (( c < stack[-1] and len(s) - i + len(stack) > k and (stack[-1] != letter or strCnt + stackCnt > repetition))                     or  stackCnt + k - len(stack)  < repetition) :
                    stackCnt  -=  1 if stack.pop() == letter else 0
            if len(stack) < k :
                stackCnt += 1 if c == letter else 0
                stack.append(c)
                
            strCnt -= 1 if c == letter else 0
        return "".join(stack)     