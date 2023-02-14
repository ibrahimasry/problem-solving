class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a = a[::-1]
        b = b[::-1]
        i = j = 0
        while carry or i < len(a) or j < len(b):
            c1 = 0 if i >= len(a) else int(a[i])
            c2 = 0 if j >= len(b) else int(b[j])
            curr = c1 + c2 + carry
            res += str(curr % 2)
            carry = curr // 2
            i += 1
            j += 1
            
        return res[::-1]