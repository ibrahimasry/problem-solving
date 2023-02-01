class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            str2,str1=str1,str2
        for i in range(len(str2),0,-1):
            curr = str2[:i]
            count2 = len(str2) // i
            count1 = len(str1) // i
            if curr * count2 == str2 and curr * count1 == str1:
                return curr
        return ""