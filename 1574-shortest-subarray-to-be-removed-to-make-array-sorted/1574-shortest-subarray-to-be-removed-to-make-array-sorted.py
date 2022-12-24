class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        while l < len(arr) - 1 and arr[l] <= arr[l+1]:
            l += 1
        if l == len(arr) - 1:
            return 0
        while r > 0 and arr[r] >= arr[r-1]:
            r -= 1
        i = 0
        j = r
        res = min(r, len(arr) - l -1)
        while i <= l and j < len(arr):
            if arr[i] <= arr[j]:
                res = min(j-i-1, res)
                i += 1

            else :
                j += 1
        return res