class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        
        
        def topo(graph, indegrees):
            queue = deque()
            for i, v in enumerate(indegrees):
                if v == 0:
                    queue.append(i)
            ans = []
            while queue :
                curr = queue.popleft()
                ans.append(curr)
                for nei in graph[curr]:
                    indegrees[nei] -= 1
                    if indegrees[nei] == 0:
                        queue.append(nei)
            return ans if len(ans) == len(indegrees) else []
        for item, groupId in enumerate(group):
            if groupId == -1:
                group[item] = m
                m += 1
        items = defaultdict(list)
        itemsDegrees = [0] * n
        groups = defaultdict(list)
        groupsDegrees = [0] * (m)

        
        for u, reqs in enumerate(beforeItems):
            for v in reqs:
                if group[u] == group[v]:
                    items[v].append(u)
                    itemsDegrees[u] +=1
                else:
                    groups[group[v]].append(group[u])
                    groupsDegrees[group[u]] += 1
        sortedItems = topo(items, itemsDegrees)
        sortedGroups = topo(groups, groupsDegrees)
        if not sortedItems or not sortedGroups:
            return []
        
        
        groupToSortedItems = defaultdict(list)
        for v in sortedItems:
            groupToSortedItems[group[v]].append(v)
        ans = []
        for v in sortedGroups:
            ans.extend(groupToSortedItems[v])
        return ans