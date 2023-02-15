class Solution:
    def minimizeResult(self, expression: str) -> str:
        res = eval(expression)
        st = "(" + expression + ")"
        n = len(expression)
        s1,s2 = expression.split('+')
        for i in range(len(s1)):
            for j in range(1,len(s2)+1):
                right = ''
                if j  < len(s2):
                    right = '*'
                left = ''
                if i > 0:
                    left = '*'
                curr = s1[:i] + left + "("+ s1[i:] + "+" + s2[:j] + ")" + right + s2[j:]
                if eval(curr) <= res:
                    res= eval(curr)
                    st = s1[:i] + "("+ s1[i:] + "+" + s2[:j] + ")" +  s2[j:]

        return st