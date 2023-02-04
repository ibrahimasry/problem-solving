class Solution:
    def maximizeWin(self, p: List[int], k: int) -> int:
        count = Counter(p)
        p = sorted(list(count.keys()))
        if k == 0:
            return sum(list(sorted(count.values()))[-2:])

        fq = deque()
        sq = deque()
        for i in range(0,min(k+1,len(p))):
            n = p[i]
            if fq and n - fq[0][0] > k:
                break
            fq.append((n,count[n],i))
        for i in range(min(len(fq),len(p)), len(p)):
            n = p[i]
            if sq and n - sq[0][0] > k : break
            sq.append((n,count[n],i))
        first = currmax = sum(c for v, c,i in fq)
        second = sum(c for v,c,i in sq)

        res = first + second
        for i in range(len(fq) + len(sq) , len(p)):
            while sq and p[i] - sq[0][0] > k : 
                second -= sq.popleft()[1]
            sq.append((p[i],count[p[i]],i))
            second += count[p[i]]
            res = max(second+currmax,res)

            while  fq[-1][-1] + 1 < sq[0][-1] :
                j = fq[-1][-1] + 1
                while fq and p[j] - fq[0][0] > k :
                    first -= fq.popleft()[1]
                fq.append((p[j],count[p[j]],j))
                first += count[p[j]]
                currmax = max(first,currmax)
                res = max(second+currmax,res)

            
        return res