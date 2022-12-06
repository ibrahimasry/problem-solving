class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        
        freq = {}
        count = Counter()
        for user, id, view in zip(creators, ids, views):
            if user not in freq:
                freq[user] = (id, view)
            elif freq[user][1] < view:
                freq[user] = (id, view)
            elif freq[user][1] == view and freq[user][0] > id:
                freq[user] = id, view
            count[user] += view
        maxValue = max(count.values())
        ans = []
        for user, (id, view) in freq.items():
            if count[user] == maxValue:
                ans.append([user, id])
        return ans