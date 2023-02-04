class Solution:
    def maximizeWin(self, p: List[int], k: int) -> int:
        count = Counter(p)
        p = list(count.keys())
        # first segement
        fq = deque()
        # second segement
        sq = deque()
        
        #first queue for first  segement
        for i in range(0,min(k+1,len(p))):
            n = p[i]
            if fq and n - fq[0][0] > k:
                break
            fq.append((n,count[n],i))
            
        #second queue for second  segement

        for i in range(min(len(fq),len(p)), len(p)):
            n = p[i]
            if sq and n - sq[0][0] > k : break
            sq.append((n,count[n],i))
            
            
        first = prevMax = sum(c for v, c,i in fq)
        second = sum(c for v,c,i in sq)

        res = first + second
        for i in range(len(fq) + len(sq) , len(p)):
            #extend second segement one point forword
            while sq and p[i] - sq[0][0] > k : 
                second -= sq.popleft()[1]
            sq.append((p[i],count[p[i]],i))
            second += count[p[i]]
            res = max(second + prevMax,res)
            #extend first segement one point forword till the start of the second segement 
            #while extending update best first seg and get max res till now

            while  fq[-1][-1] + 1 < sq[0][-1] :
                j = fq[-1][-1] + 1
                while fq and p[j] - fq[0][0] > k :
                    first -= fq.popleft()[1]
                fq.append((p[j],count[p[j]],j))
                first += count[p[j]]
                prevMax = max(first,prevMax)
                res = max(second+prevMax,res)

            
        return res