class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = [int(num) for num in s.split() if num.isdigit()]
        prev = -1
        for curr in s:
            if curr <= prev:
                return False
            prev = curr
        return True
        