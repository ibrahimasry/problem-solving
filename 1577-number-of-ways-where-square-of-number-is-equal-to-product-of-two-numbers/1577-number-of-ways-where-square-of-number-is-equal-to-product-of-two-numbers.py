class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def go(nums1,nums2):
            count2 = Counter([n**2 for n in nums2])
            cnt1 = (Counter(nums1))
            keys1 = list(set(nums1))
            res = 0
            for i in range(len(keys1)):
                res += count2[keys1[i] ** 2] * (cnt1[keys1[i]]-1) * (cnt1[keys1[i]]) // 2
                for j in range(i+1,len(keys1)):
                    res += count2[keys1[i] * keys1[j]] * cnt1[keys1[i]] * cnt1[keys1[j]]
            return res
        return go(nums1,nums2) + go(nums2,nums1)