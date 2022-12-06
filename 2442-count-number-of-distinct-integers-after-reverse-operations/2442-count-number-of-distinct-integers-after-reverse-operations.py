class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        curr = set(map(str, nums))
        
        for s in list(curr):
            curr.add(s[::-1])
        curr = set(map(int, list(curr)))
        return len(curr)