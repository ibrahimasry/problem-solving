class Node:
      def __init__(self):
            self.children = [None, None]
            self.count = 0

    
class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        
        root = Node()
        def countSmaller(num, limit):
            ans = 0
            tri = root
            for i in range(14,-1,-1):
                if not tri:
                    break
                limitBit = (limit >> i) & 1
                numBit = num >> i & 1
                if limitBit == 1:
                    if tri.children[numBit]:
                        ans += tri.children[numBit].count
                    tri = tri.children[numBit ^ 1]
                else :
                    tri = tri.children[numBit]
                        
            return ans 
        def insert(num):
            tri = root
            for i in range(14, -1, -1):
                curr = (num >> i) & 1
                if  not tri.children[curr] :
                    tri.children[curr] = Node()
                tri.children[curr].count += 1
                tri = tri.children[curr]
        res = 0

        for num in nums:
            res +=  countSmaller(num, high + 1) - countSmaller(num, low)
            insert(num)
         
        return res
