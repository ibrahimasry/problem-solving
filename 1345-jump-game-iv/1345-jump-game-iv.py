class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        valToIdx = defaultdict(list)
        
        for i, v in enumerate(arr):
            valToIdx[v].append(i)
        queue = deque([0])
        seen = set()
        seen.add(0)
        ans = 0
        
        n = len(arr)
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == n-1:
                    return ans
                if curr > 0 :
                    if curr - 1 not in seen:
                        seen.add(curr-1)
                        queue.append(curr-1)
                if curr + 1 not in seen:
                    seen.add(curr+1)
                    queue.append(curr+1)
                for id in valToIdx[arr[curr]]:
                    if id in seen: continue
                    seen.add(id)
                    queue.append(id)
                del valToIdx[arr[curr]]
            ans += 1
        