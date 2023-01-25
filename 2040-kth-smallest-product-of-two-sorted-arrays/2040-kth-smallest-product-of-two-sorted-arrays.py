from bisect import bisect, bisect_left

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        def check(x):
            total = 0
            for n1 in nums1:
                if n1 > 0: total += bisect(nums2, x//n1)
                if n1 < 0: total += len(nums2) - bisect_left(nums2, ceil(x/n1))
                if n1 == 0 and x >= 0: total += len(nums2)

            return total

        beg, end = -10**10 - 1, 10**10 + 1

        while beg < end:
            mid = (beg + end)//2
            if check(mid) >= k:
                end = mid
            else:
                beg = mid + 1

        return beg 
        