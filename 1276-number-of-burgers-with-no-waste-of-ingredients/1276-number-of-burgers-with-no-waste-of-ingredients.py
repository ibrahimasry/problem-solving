class Solution:
    def numOfBurgers(self, t: int, c: int) -> List[int]:
         #big + small = chese
        # 2big + small = tomato/2
        
        #big = tomato/2 - chse
        #small = 2chese - tomato/2
        
        if t / 2 - c < 0 or 2 * c - t /2 <0 or t % 2:
            return []
        
        return [t//2-c, 2*c -t//2]
        
