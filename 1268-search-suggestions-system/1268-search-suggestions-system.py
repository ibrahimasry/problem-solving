class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        n = len(products)
        l = 0
        r = n - 1
        res = []
        
        for i, c in enumerate(searchWord):
            
            while l <= r and (len(products[l]) - 1 < i or products[l][i] != c):
                l += 1
            while l <= r and (len(products[r]) - 1 < i or products[r][i] != c):
                r -= 1
                
            cand = r - l + 1
            
            res.append([])
            for j in range(min(3,cand)):
                res[-1].append(products[l+j])
        return res

                