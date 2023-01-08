class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        res = 1
        points.sort()
        for i in range(n):
            p1,p2= points[i]
            count = defaultdict(int)
            overlap  = 0

            for j in range(i+1,n):
                p3,p4 = points[j]
                if p1 == p3 and p4 == p2:
                    overlap += 1
                elif p2 == 0 and p4 == 0:
                    count[(1,0)] += 1
                elif p1 == 0 and p3 == 0:
                    count[(0,1)] += 1
                else:
                    x,y = p1-p3,p2-p4
                    z = gcd(abs(x),abs(y))
                    count[(x//z,y//z)] += 1
                values = list(count.values())
                values.append(0)
                maxVal = max(values)
            
                res = max(res,maxVal + 1 + overlap)
        return res