class Solution:
    def totalStrength(self, arr: List[int]) -> int:
        N = len(arr)
        stack = []
        right = [N] * len(arr)
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
               right[stack.pop()] = i
            stack.append(i)

        stack = []
        left = [-1] * len(arr)
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]] >= arr[i]:
              left[stack.pop()]  = i
            stack.append(i)

        pre =  list(accumulate(accumulate(arr), initial = 0))
        total = 0
        for i in range(N):
            l = left[i]
            r = right[i]
            rSum = (pre[r] - pre[i]) * (i-l)
            lSum = (pre[i] - pre[max(l,0)]) * (r-i)
            total += arr[i] * (rSum - lSum)
        return total % (10**9 +7)
