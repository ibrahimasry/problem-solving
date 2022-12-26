class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        first = -1
        
        i = len(arr) - 1
        while i > 0:
            if arr[i] < arr[i-1]:
                first = i-1
                break
            i -= 1
        if first == -1:
            return arr
        second = -1
        i = len(arr) - 1
        while i > 0:
            if arr[i] < arr[first] and arr[i] != arr[i-1]:
                second = i
                break
            i -= 1
        arr[first], arr[second] = arr[second],arr[first]
        return arr
        
        