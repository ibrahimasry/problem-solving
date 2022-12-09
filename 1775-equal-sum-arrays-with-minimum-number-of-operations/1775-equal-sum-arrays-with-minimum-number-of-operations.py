class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        if sum1 == sum2:
            return 0
        diff = abs(sum1-sum2)
        
        arr = []
        if sum1 < sum2:
            arr = [6-x for x in nums1] + [abs(1-x) for x in nums2]
        else :
            arr = [abs(1-x) for x in nums1] + [6-x for x in nums2]
        arr.sort(reverse=True)
        
        moves = 0
        for x in arr:
            diff -= x
            moves += 1
            if diff <= 0 :
                return moves
        return -1