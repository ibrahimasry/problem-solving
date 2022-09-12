class DetectSquares:

    def __init__(self):
        self.pointsPerY = defaultdict(Counter)
        

    def add(self, point: List[int]) -> None:
        x, y = point
        self.pointsPerY[y][x] +=1
        

    def count(self, point: List[int]) -> int:
        
        x1 , y = point
        points = self.pointsPerY[y]
        ans = 0
        for x2 in points.keys():
            if x1 == x2 :
                continue
            ans += self.pointsPerY[y][x2] * self.pointsPerY[y-abs(x1-x2)][x2] * self.pointsPerY[y-abs(x1-x2)][x1]
            ans += self.pointsPerY[y][x2] * self.pointsPerY[y+abs(x1-x2)][x2] * self.pointsPerY[y+abs(x1-x2)][x1]
        return ans     

        
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)