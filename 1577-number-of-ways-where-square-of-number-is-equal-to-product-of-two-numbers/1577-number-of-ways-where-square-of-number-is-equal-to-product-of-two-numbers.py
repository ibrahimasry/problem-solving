class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def go(nums1,nums2):
            count2 = Counter([n**2 for n in nums2])
            cnt1 = (Counter(nums1))
            keys1 = sorted(list(set(nums1)))
            res = 0
            for i in range(len(keys1)):
                for j in range(i,len(keys1)):
                    if i != j  :
                        res += count2[keys1[i] * keys1[j]] * cnt1[keys1[i]] * cnt1[keys1[j]]
                    if i == j  :
                        res += count2[keys1[i] * keys1[j]] * (cnt1[keys1[i]]-1) * (cnt1[keys1[i]]) // 2
            return res
        return go(nums1,nums2) + go(nums2,nums1)