class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        pre = list(accumulate(packages, initial=0))
        for box in boxes:
            box.sort()
        ans = inf
        
        for box in boxes:
            start = 0
            wasted = 0
            if box[-1] < packages[-1]:
                continue
            for size in box:
                r = bisect.bisect(packages,size,start)
                wasted += size * (r-start) - (pre[r]-pre[start])
                start = r
            if start == len(packages):
                ans = min(wasted, ans)
                ans %= 10**9 + 7
        return ans if ans != inf else -1