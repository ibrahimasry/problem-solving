class Solution:
    def largestVariance(self, s: str) -> int:
        if len(set(s)) == 1 or len(set(s)) == len(s):
            return 0
        seen = set(s)
        res = 0
        chrToIdx = defaultdict(list)
        for i , c in enumerate(s):
            chrToIdx[c].append(i)
        counts = Counter(s)
        for c1 in chrToIdx:
            for c2 in chrToIdx:
                if c1 == c2:
                    continue
                arr = []
                i = j = 0
                first = chrToIdx[c1]
                second = chrToIdx[c2]
                while i < len(first) and j < len(second):
                    if first[i] < second[j]:
                        arr.append(first[i])
                        i += 1
                    else :
                        arr.append(second[j])
                        j += 1
                arr += first[i:] + second[j:]
                curr = 0
                total = 0
                small = 0
                currSmall = 0
                for i in arr:
                    c = s[i]
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
                        total = max(total , curr)
                res = max(res, total)
                    
        return res