class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        tree = defaultdict(list)
        for node, parent in enumerate(parents):
            tree[parent].append(node)
        seen = set()
        def dfs(node):
            if nums[node] in seen:
                return
            seen.add(nums[node])
            for nei in tree[node]:
                dfs(nei)
        if 1 not in nums:
            return [1] * len(parents)
        res = [1] * len(parents)
        node1 = nums.index(1)
        curr = 1

        while node1 != -1:
            dfs(node1)
            while curr in seen:
                curr += 1
            res[node1] = curr
            node1 = parents[node1]
        return res
        