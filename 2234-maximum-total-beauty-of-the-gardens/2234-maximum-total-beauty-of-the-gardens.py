class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        flowers = [min(target, a) for a in flowers]
        flowers.sort()

        n = len(flowers)
        pre = [0] * n

        for i in range(1,n):
            diff = flowers[i] - flowers[i-1]
            pre[i] += pre[i-1] + diff*i
        if min(flowers) == target: return full * n
        if newFlowers >= target * n - sum(flowers):
            return max(full*n, full * (n-1) + partial * (target - 1) )

        j = n - 1
        while  flowers[j] == target:
            j -= 1
        
        res = 0
        while newFlowers >= 0:
            left = bisect.bisect(pre, newFlowers,hi=j+1)
            base = flowers[left-1]
            sur = (newFlowers - pre[left-1]) // (left)
            mn = base + sur
            res = max((n-j-1) * full + mn*partial,res)
            newFlowers -= (target - flowers[j])
            j -= 1

        return res
            
        