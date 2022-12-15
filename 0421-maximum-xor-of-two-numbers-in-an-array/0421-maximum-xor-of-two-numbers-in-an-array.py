class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        class Trie:
            tri = {}

            def insert(self, n):
                tri = self.tri 
                for i in range(31,-1,-1):
                    node = (n >> i) & 1

                    if not (node in tri):
                        tri[node] = {}
                    tri = tri[node]
            def search(self, n):

                res = 0
                tri = self.tri
                for i in range(31,-1,-1):
                    node = (n >> i) & 1 
                    req = 0 if node == 1 else 1
                    
                    if req in tri:
                        tri = tri[req]
                        res = res | ((req) << i)
                    else :
                        tri = tri[node]
                        res = res | ((node) << i)


                        
                return res
        tri = Trie()
        for n in nums:
            tri.insert(n)
        res = 0

        for n in nums:
            curr = tri.search(n)
            res = max(res, curr^n)
        return res
