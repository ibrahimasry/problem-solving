class Solution:
    def compress(self, chars: List[str]) -> int:
        r = 0
        left = 0
        for i in range(len(chars)):
            if i == (len(chars) - 1) or chars[i] != chars[i+1]:
                l = len(str(i - r + 1))
                chars[left] = chars[r]
                left += 1
                if i > r:
                    chars[left:left+l] = list(str(i - r + 1))
                    left += l
                r = i + 1
        return left
        