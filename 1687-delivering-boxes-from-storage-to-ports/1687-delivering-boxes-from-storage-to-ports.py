class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        
        
        n = len(boxes)
        dp = [sys.maxsize] * (n+1)
        dp[0] = 0
        left = 0
        weight = 0
        trips = 2
        for right in range(n):
            weight += boxes[right][1]
            if right > 0 and boxes[right][0] != boxes[right-1][0]:
                trips += 1
            while weight > maxWeight or right-left >= maxBoxes or (right > left and dp[left] == dp[left+1]):
                weight -= boxes[left][1]
                if (boxes[left][0] != boxes[left+1][0]):
                    trips -= 1
                left += 1
            dp[right+1] = dp[left] + trips
        return dp[-1]