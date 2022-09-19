class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        
        
        total = sum(arr)
        if total == 0 :
            return [0, len(arr) -1]
        if total % 3 != 0 :
            return [-1, -1]
        target = total // 3
        p1 = 0
        p2 = 0
        p3 = 0
        curr = 0
        for i,  n in enumerate(arr) :
            if n == 0 : continue
            if curr == 0  :
                p1 = i
            elif curr == target  :
                p2 = i
            elif curr == target * 2:
                p3 = i
            curr += 1
    
                
        oldp2 = p2
        oldp3 = p3
        oldp1 = p1
        while p3  < len(arr) and p2 < oldp3 and p1 < oldp2:
            if arr[p1] != arr[p2] or arr[p1] != arr[p3] :
                return [-1, -1]
            p2 += 1
            p3 += 1
            p1 += 1
        if p3 != len(arr) : return [-1, -1]
        else : return [p1-1, p2]     