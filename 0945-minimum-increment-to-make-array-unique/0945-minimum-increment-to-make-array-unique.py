class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        distinct = sorted(list(set(nums)))
        
        freq = Counter(nums)
        
        freq = {k:v for k, v in freq.items() if v > 1}
        dup = sorted(freq.keys())

        added = [distinct[0]]
        moves = 0
        
        i = 0
        j = 1
        
        while  len(freq):
            curr = (added[-1] - dup[i]) + 1 + dup[i]

            if  j == len(distinct) or (dup[i] != -1 and distinct[j] > dup[i] and  curr < distinct[j])  :
                val = dup[i]
                freq[val] -= 1
                added.append(curr)
                moves += curr - dup[i]
                if freq[val] == 1:
                    del freq[val]
                    dup[i] = -1
                    i += 1


            else :
                added.append(distinct[j])
                j += 1
                
        return moves