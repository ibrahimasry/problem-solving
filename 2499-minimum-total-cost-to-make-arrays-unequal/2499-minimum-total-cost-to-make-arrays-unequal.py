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
        dom = max(c1.keys() , key=lambda x:c1[x])
        countOfDom = c1[dom] 
        dupSum = sum(c1.values())
        if dupSum - countOfDom >=countOfDom:
            return res
        
        countOfDom = countOfDom - (dupSum - countOfDom)
        for i in range(n):
            if nums1[i] == nums2[i] or nums1[i] == dom or nums2[i] == dom:
                continue
            countOfDom -= 1
            res += i
            if countOfDom == 0:
                return res
        return -1
                