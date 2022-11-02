class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        
        r = len(arr)
        ans = sys.maxsize
        s = set()
        for i in range(r):
            temp = {arr[i] & curr for curr in s} | {arr[i]}
            for curr in temp:
                ans = min(ans, abs(curr-target))

                if curr == target:
                    return 0
            s = temp
        return ans