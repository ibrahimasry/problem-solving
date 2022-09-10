class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        
        
        
        
        def dfs(sums):
            if 0 not in sums :
                return []
            if len(sums) == 2 :
                sums.remove(0)
                return [sums[0]]
            x = sums[-1] - sums[-2]
            sums1 = []
            counts = Counter(sums)
            for n in sums[::-1]:
                m = n - x
                if counts[n] > 0 :
                    if counts[m] > 0 :
                        sums1.append(m)
                        counts[m] -= 1
                        counts[n] -= 1
                    else : 
                        break
            ans1 = [x]
            if len(sums) // 2 == len(sums1) :
                ans1 += dfs(sums1[::-1])
            sums2 = []
            counts = Counter(sums)
            for n in sums:
                m = n + x
                if counts[n] > 0 :
                    if  counts[m] > 0 :
                        sums2.append(m)
                        counts[m] -= 1
                        counts[n] -= 1
                    else :
                        break
            ans2 = [-x]
            if len(sums) // 2 == len(sums2) :
                ans2 += dfs(sums2)
                
            return ans2 if len(ans2) > len(ans1)  else ans1    
        sums.sort()
         
        return dfs(sums)

                
            
            
        