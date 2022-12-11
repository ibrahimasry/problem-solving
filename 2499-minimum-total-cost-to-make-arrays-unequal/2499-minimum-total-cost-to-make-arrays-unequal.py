class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        c1 = Counter()
        res = 0
        for i in range(n):
            if nums1[i] == nums2[i]:
                c1[nums1[i]] += 1
                res += i
        if len(c1) == 0:
            return 0
        maxNumber =  max(c1.keys() , key=lambda x:c1[x])
        countOfMax = c1[maxNumber] 
        totalSum = sum(c1.values())
        if totalSum - countOfMax >= countOfMax:
            return res
        
        countOfMax = countOfMax - (totalSum - countOfMax)
        for i in range(n):
            if nums1[i] == nums2[i] or nums1[i] == maxNumber or nums2[i] == maxNumber:
                continue
            countOfMax -= 1
            res += i
            if countOfMax == 0:
                return res
        return -1
                