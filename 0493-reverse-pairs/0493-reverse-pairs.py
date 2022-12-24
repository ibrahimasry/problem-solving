class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        
        def dfs(arr):
            nonlocal count
            if not arr or len(arr) == 1 :
                return arr
            m = len(arr)//2
            left = dfs(arr[:m])
            right = dfs(arr[m:])
            
            l = 0
            r = 0
            arr = []
            curr = 0
            last = right[r]
            p = 0
            k = r
            m = l

            while m < len(left) and k < len(right):
                if  left[m] > 2*right[k]:
                    count += (len(left) - m)
                    k += 1
                else :
                    m += 1
            while r < len(right) and l < len(left):
                if left[l] < right[r]:
                    arr.append(left[l])
                    l += 1
                else :
                    arr.append(right[r])
                    r += 1
            arr += left[l:] + right[r:]
            return arr
        dfs(nums)
        return count
                    