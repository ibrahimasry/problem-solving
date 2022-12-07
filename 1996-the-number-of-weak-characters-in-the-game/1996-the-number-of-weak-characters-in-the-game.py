class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        properties.sort()
        lastx = -10
        maxy = -1
        count = 0
        pmaxy = -1
        for x, y in properties[::-1]:
            if x != lastx :
                lastx = x
                maxy = pmaxy
            pmaxy = max(pmaxy, y)
            if y < maxy:
                count += 1
        return count
            