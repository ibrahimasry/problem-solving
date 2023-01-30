class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        seen = set(ideas)
        counter = defaultdict(lambda: defaultdict(int))
        for name in ideas:
            for c in string.ascii_lowercase:
                if c + name[1:] in seen: continue
                counter[name[0]][c] += 1
        res  = 0
        
        for name in ideas:
            for c in string.ascii_lowercase:
                if c + name[1:] in seen: continue
                res += counter[c][name[0]]
        return res