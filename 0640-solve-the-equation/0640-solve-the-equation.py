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
                if curr == "-":
                    prev = -1
                else:
                    prev = 1 
            elif curr == "=":
                prev = 1
                flag   = 1
                flagx  = -1
            
            elif curr == "x":
                x.append(prev * flagx)
            else :
                n = 0
                while i < k and equation[i].isdigit():
                    n = n * 10 + int(equation[i])
                    i += 1
                i -= 1
                if (i+1 < k  and equation[i+1] != "x" ) or i+1 == k:
                    nums.append(prev * n * flag)
                elif i + 1 < k and equation[i+1] == "x" :
                    x.append(prev * n * flagx)
                    i += 1
                n = 1

                    

            i += 1
        if sum(x) == 0 and sum(nums) != 0:
            return "No solution"
        if sum(x) == 0:
            return "Infinite solutions"
        return "x=" + str(sum(nums) //sum(x))