class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        
        c = Counter()
        mx = 0
        for s, m in zip(senders, messages):
            c[s] += len(m.split(" "))
            mx = max(mx, c[s])
        sender = ''    
        for k, v in c.items():
            if v == mx and sender < k:
                sender = k
        return sender
