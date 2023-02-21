class Solution:
    def threeSumMulti(self, keys: List[int], target: int) -> int:
        
        count = Counter(keys)
        keys = sorted(count)
        res = 0
        n  =  len(keys) - 1
        for i , x in enumerate(keys):
            t = target - x
            j = i
            k = n 
            
            while j <= k:
                if keys[j] + keys[k] > t:
                    k -= 1
                elif keys[j] + keys[k] < t:
                    j += 1
                else :
                    
                    if i < j < k:
                        res += count[keys[i]]  * count[keys[j]] * count[keys[k]]
                    elif i == j < k:
                        res += count[keys[i]] * (count[keys[i]] - 1) * count[keys[k]] // 2
                    elif i < j == k:
                        res += count[keys[j]] * (count[keys[j]] - 1) * count[keys[i]] // 2
                    elif i == j == k and count[keys[j]] >= 2:
                        res += comb(count[keys[j]],3)

                    k -= 1
                    j += 1
        return res % (10**9 + 7)



                