class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        freq = Counter(tasks)
        
        maxKey,maxKeyValue = max(freq.items(),key=lambda x:x[1])
        total = sum(freq.values())
        
        maxKeyCount = sum([1 for k, v in freq.items() if v == maxKeyValue])
        gap = (n - (maxKeyCount-1)) * (maxKeyValue -1)
        gap -= (total- maxKeyCount * maxKeyValue)
        gap = 0 if gap < 0 else gap
        return total + gap
        
        return res