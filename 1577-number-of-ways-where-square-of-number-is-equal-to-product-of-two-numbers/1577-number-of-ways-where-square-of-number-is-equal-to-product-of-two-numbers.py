class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        count1 = Counter([n**2 for n in nums1])
        count2 = Counter([n**2 for n in nums2])
        cnt1 = (Counter(nums1))
        cnt2 = (Counter(nums2))
        keys1 = sorted(list(set(nums1)))
        keys2 = sorted(list(set(nums2)))
        res = 0
        n1 = len(nums1)
        n2 = len(nums2)
        for i in range(len(keys1)):
            for j in range(i,len(keys1)):
                if i != j  :
                    res += count2[keys1[i] * keys1[j]] * cnt1[keys1[i]] * cnt1[keys1[j]]
                if i == j  :
                    res += count2[keys1[i] * keys1[j]] * (cnt1[keys1[i]]-1) * (cnt1[keys1[i]]) // 2
        for i in range(len(keys2)):
            for j in range(i,len(keys2)):
                if i != j  :
                    res += count1[keys2[i] * keys2[j]] * cnt2[keys2[i]] * cnt2[keys2[j]]
                if i == j  :
                    res += count1[keys2[i] * keys2[j]] * (cnt2[keys2[i]]-1) * (cnt2[keys2[j]]) // 2

        return res