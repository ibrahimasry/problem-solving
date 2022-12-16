class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        i = 0
        j = 0
        n = len(nums1)
        m = len(nums2)
        sum1 = 0
        sum2 = 0
        res = 0
        while i < n or j < m:
            
            if (i < n and j < m and nums1[i] < nums2[j]) or (i < n and j == m):
                
                sum1 += nums1[i]
                i += 1
            elif (i < n and j < m and nums1[i] > nums2[j]) or (j < m and i == n):
                sum2 += nums2[j]
                j += 1
            else:
                res += max(sum1, sum2) + nums1[i]
                i += 1
                j += 1
                sum1 = 0
                sum2 = 0
        return (res + max(sum1, sum2)) % (10 ** 9 + 7)