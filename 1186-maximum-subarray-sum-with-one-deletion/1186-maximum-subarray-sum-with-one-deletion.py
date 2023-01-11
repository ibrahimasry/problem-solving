class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        
        def getMaxAll(arr):
            run = res = minn = 0
            
            for n in arr:
                if run <= 0 :
                    run = minn = 0
                run += n
                res = max(run-minn,res)
                minn = min(minn, n)
            return res
        def getMax(arr):
            prefix = [0] + list(accumulate(arr))
            currMax = -inf
            running = -inf
            currMin = inf
            i = 0
            for j, n in enumerate(arr):
                if n < 0  and n <= currMin:
                    if currMin == inf:
                        currMin = n
                        i = j
                    else:
                        if running == -inf:
                            running = currMin
                        else :
                            if running + currMin < prefix[j] - prefix[i+1]:
                                running = prefix[j] - prefix[i]
                            else :
                                running += currMin
                        i = j

                        currMin = n
                elif running + n < n:
                    running = n
                    currMin = inf
                     
                else :
                    running += n
                currMax = max(running ,currMax)
            return 0 if currMax == -inf else currMax
        if min(arr) >= 0 or len(arr) == 1 : 
            return sum(arr)
        if not any([1 for n in arr if n > 0]):
            return max(arr)
            
        return max(getMax(arr), getMaxAll(arr) , getMax(arr[::-1]))