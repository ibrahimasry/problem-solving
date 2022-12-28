class Solution:
    def solveEquation(self, equation: str) -> str:
        x = []
        nums = []
        prev = 1
        flagx = 1
        flag = -1
        n = 0
        i = 0
        equation = "+" + equation + "+"
        k = len(equation)

        while i < k:
            curr = equation[i]
            if curr in ["-", "+"]:
                n = 1
                if curr == "-":
                    prev = -1
                else:
                    prev = 1 
            elif curr == "=":
                n = 1
                prev = 1
                flag   = 1
                flagx  = -1
            
            elif curr == "x":
                x.append(prev * n * flagx)
                n = 1
            else :
                n = 0
                while i < k and equation[i].isdigit():
                    n = n * 10 + int(equation[i])
                    i += 1
                i -= 1
                if i < k -1 and equation[i+1] != "x":
                    nums.append(prev * n * flag)

            i += 1
        if sum(x) == 0 and sum(nums) != 0:
            return "No solution"
        if sum(x) == 0:
            return "Infinite solutions"
        return "x=" + str(sum(nums) //sum(x))