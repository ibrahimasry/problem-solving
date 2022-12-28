class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = [0,0]
        for op in operations:
            if not op.isdigit() and len(op) == 1:
                if op == "C":
                    stack.pop()
                if op == "D":
                    stack.append(stack[-1] * 2)
                if op == "+":
                    stack.append(stack[-1] + stack[-2])
            else :
                stack.append(int(op))
        return sum(stack)
                