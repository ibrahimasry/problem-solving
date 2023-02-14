class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        mx = startPos+2
        indVal = defaultdict(int)

        for i , a in fruits:
            mx=max(i,mx)
            indVal[i] = a
        pre = [0] * (mx+2)
        for i in range(len(pre)-1):
            pre[i+1] += indVal[i]
            pre[i+1] += pre[i]
        best = 0
        for i in range(k+1):
            forward  = k - i
            backward = (k - forward)//2
            right = min(len(pre) - 1, startPos + forward+1)
            left = max(0, startPos - backward)
            curr = pre[right] - pre[left]
            best = max(curr , best)
        for i in range(k+1):
            b  = k - i
            f = (k - b)//2
            right = min(len(pre) - 1, startPos + f+1)
            left = max(0, startPos - b)
            curr = pre[right ] - pre[left]
            best = max(curr , best)
        return best