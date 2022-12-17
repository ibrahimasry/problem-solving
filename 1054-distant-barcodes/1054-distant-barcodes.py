class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n = len(barcodes)
        
        ans = [0] * (n)
        count = sorted(list(Counter(barcodes).items()), key=lambda  x:-x[1])
        pos = 0
        maxVal = count[0][1]
        for k, v in count:
            for i in range(v):
                ans[pos] = k
                pos = (2 + pos if 2 + pos < n else 1)
                
        
        return ans