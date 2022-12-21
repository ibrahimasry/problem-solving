class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        
        pre = {}
        running = 0
        for i,n in enumerate(arr):
            if i == len(arr) -1:
                break
            running += n 
              
            if running % 2 == 0 and running // 2 in pre and total - running == running // 2:
                return True
            pre[running] = True
        return False