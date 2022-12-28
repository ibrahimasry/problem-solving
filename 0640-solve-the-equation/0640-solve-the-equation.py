class Solution:
    def solveEquation(self, equation: str) -> str:
        x = 0
        nums = 0
        sign = 1
        flipx = 1
        flipn = -1
        i = 0
        k = len(equation)

        while i < k:
            curr = equation[i]
            if curr in ["-", "+"]:
                if curr == "-":
                    sign = -1
                else:
                    sign = 1 
            elif curr == "=":
                sign      = 1
                flipn    *= -1 
                flipx    *= -1
            
            elif curr == "x":
                x += sign * flipx
            else :
                n = 0
                while i < k and equation[i].isdigit():
                    n = n * 10 + int(equation[i])
                    i += 1
                i -= 1
                if (i+1 < k  and equation[i+1] != "x" ) or i+1 == k:
                    nums += sign * n * flipn
                if i + 1 < k and equation[i+1] == "x" :
                    x += n * sign * flipx
                    i += 1
            i += 1
        if x == 0 and nums != 0:
            return "No solution"
        if x == 0:
            return "Infinite solutions"
        return "x=" + str(nums // x)