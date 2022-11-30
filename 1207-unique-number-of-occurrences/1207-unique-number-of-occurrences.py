class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        occ = set(count.values())
        
        return len(occ) == len(count)