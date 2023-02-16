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

        j = bisect.bisect_left(flowers,target) - 1
        
        while newFlowers >= target - flowers[j]:
            newFlowers -= target - flowers[j]
            j -= 1
        cnt = n - j - 1

        res = 0
        while True:
            left = bisect.bisect(pre, newFlowers, hi=j+1)
            mn = 0
            if left > 0:
                base = flowers[left-1]
                sur = (newFlowers - pre[left-1]) // (left)
                mn = base + sur
            res = max(cnt * full + mn*partial,res)
            if not cnt:
                break
            j += 1
            newFlowers += (target - flowers[j])
            cnt -= 1

        return res
            
        