class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return [int(s) for s in str(int(''.join([str(c) for c in num])) + k)]