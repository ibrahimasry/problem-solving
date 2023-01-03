class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        small = []
        big = []
        eq = []
        for n in nums:
            if n < pivot:
                small.append(n)
            elif n > pivot:
                big.append(n)
            else :
                eq.append(n)
        return small + eq + big
