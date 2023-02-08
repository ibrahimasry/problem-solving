class Solution:
    def largestVariance(self, s: str) -> int:
        if len(set(s)) == 1 or len(set(s)) == len(s):
            return 0
        res = 0
        counts = Counter(s)
        for c1 in counts:
            for c2 in counts:
                if c1 == c2 :
                    continue
                curr = 0
                total = 0
                small = 0
                currSmall = 0
                for c in s:
                    if c == c1:
                        curr -= 1
                    elif c == c2:
                        curr += 1
                    small += c == c1
                    currSmall += c == c1
                    if curr < 0:
                        if small == counts[c1]:
                            curr = -1 
                            currSmall = 1
                        else :
                            curr = 0
                            currSmall = 0
                    if currSmall > 0:
                        if curr > res:
                            res = curr
                    
        return res