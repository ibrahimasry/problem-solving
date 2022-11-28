class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        
        boundries = defaultdict(list)
        
        for i, c in enumerate(s):
            if boundries[c]:
                boundries[c][1] = i
            else :
                boundries[c] = [i, i]
        intervals = set()
        
        for i in range(0, 26):
            c = chr(i + ord('a'))
            if boundries[c]:
                start , end = boundries[c]
                i = start 
                while i <= end and start == boundries[c][0]:
                    start = min(boundries[s[i]][0], start)
                    end = max(boundries[s[i]][1], end)
                    i += 1
                if start == boundries[c][0] :
                    intervals.add((start, end))

        intervals = list(intervals)
        intervals.sort(key=lambda a:a[1])
        
        prev = intervals[0]
        res = [s[prev[0]:prev[1]+1]]
        for start , e in intervals[1:]:
            if start > prev[1] :
                res.append(s[start:e+1])
            prev = [start, e]
        return res

                