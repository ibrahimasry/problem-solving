class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        parent = list(range(len(source)+1))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            r1 = find(x)
            r2 = find(y)
            if r1 != r2:
                parent[r2] = r1
                return True
            return False
        for x, y in allowedSwaps:
            union(y, x)
        group = defaultdict(list)
        for i , c in enumerate(source):
            group[find(i)].append(i)
        ans = 0
        for _ , ind in group.items():
            count = defaultdict(int)
            for i in ind:
                count[source[i]] += 1
                count[target[i]] -= 1
            ans += sum(c for c in count.values() if c > 0)
        return ans