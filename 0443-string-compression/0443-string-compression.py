class Solution:
    def compress(self, chars: List[str]) -> int:
        r = 0
        left = 0
        for i in range(1,len(chars)):
            if chars[i] != chars[r]:
                if i - r == 1:
                    chars[left] = chars[r]
                    left += 1

                    r = i
                    
                else:
                    l = len(str(i - r))
                    chars[left] = chars[r]
                    left += 1
                    chars[left:left+l] = [c for c in str(i - r)]
                    left += l
                    r = i
        if len(chars) - r > 1:
            l = len(str(len(chars) - r))
            chars[left] = chars[r]

            chars[left+1:left+1+l] = [c for c in str(len(chars) - r)]
            del chars[left+1+l:]
        else :
            chars[left] = chars[r]
            del chars[left+1:]
        