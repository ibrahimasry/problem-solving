class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2 = sorted([(v, i) for i, v in enumerate(nums2)])
        n = len(nums1)
        res = [-1]  * n
        queue = []
        i = 0
        j = 0
        while i < n:
            if nums1[i] > nums2[j][0]: 
                res[nums2[j][1]] = nums1[i]
                j += 1
            else :
                queue.append(i)
            i += 1
        j = 0
        for i in range(n):
            if res[i] == -1:
                res[i] = nums1[queue[j]]
                j += 1
        return res