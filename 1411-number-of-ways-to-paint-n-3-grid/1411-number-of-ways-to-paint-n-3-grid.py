class Solution:
    def numOfWays(self, n: int) -> int:
    
        a121 = 6
        a213 = 6
        
        for i in range(n-1):
            a121  , a213 = 3 * a121 + 2 * a213 , 2 * a121 + 2 * a213
            
        return (a121 + a213) % (10 ** 9 + 7)