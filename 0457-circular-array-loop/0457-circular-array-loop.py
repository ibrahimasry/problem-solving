class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dfs(curr, visited):
            if visited[curr] == 2:
                return False
            if visited[curr] == 1:
                return True
            visited[curr] = 1
            nextn = (curr + nums[curr] + len(nums)) % len(nums)
            if nums[nextn] * nums[curr] < 0 or nextn == curr:
                visited[curr] = 2
                return False
            if dfs(nextn, visited):
                return True
            visited[curr] = 2
            return False
        visited = [0] * len(nums)
        
        for i in range(len(nums)):
            if not visited[i] and dfs(i,visited):
                return True
        return False