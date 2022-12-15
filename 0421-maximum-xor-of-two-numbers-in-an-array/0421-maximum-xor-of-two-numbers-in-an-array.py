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
                    req = 0 if node == 1 else 0
                    if node == 0:
                        if 1 in tri:
                            tri = tri[1]
                            res = res | ((1) << i)
                        else :
                            tri = tri[0]
                            res = res | ((0) << i)
                    else :
                        if 0 in tri:
                            tri = tri[0]
                            res = res | ((0) << i)
                        else :
                            tri = tri[1]
                            res = res | ((1) << i)


                        
                return res
        tri = Trie()
        for n in nums:
            tri.insert(n)
        res = 0

        for n in nums:
            curr = tri.search(n)
            print(curr)
            res = max(res, curr^n)
        return res
