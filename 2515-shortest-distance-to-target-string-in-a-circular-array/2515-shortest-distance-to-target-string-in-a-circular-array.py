class Solution:
    def closetTarget(self, words: List[str], target: str, s: int) -> int:
        n = len(words)
        if target not in set(words):
            return -1
        res = n
        last = inf
        s1 =  s + n 

        for i in range(n):
            if words[i] == target:
                last = i
            if last != inf:
                res = min(res, min(last + n - s, min(abs(last - s), abs(last-s1))))

        return res