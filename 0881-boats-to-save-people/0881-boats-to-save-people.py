class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        
        people.sort()
        
        i = 0
        j = len(people) - 1
        res = 0
        
        while i < j:
            if people[j] + people[i] <= limit:
                j -= 1
                i += 1
            else:
                j -= 1
            res += 1
        return res if j < i else res + 1