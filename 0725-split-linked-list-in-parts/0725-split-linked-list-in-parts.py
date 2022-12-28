# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        res = []
        l = 0
        node = head
        while head:
            head = head.next
            l += 1
        for i in range(k, 0,-1):
            curr = ceil(l/i)
            l -= curr
            part = node
            prev = None
            for j in range(curr):
                prev = node
                node = node.next
            if prev:
                prev.next = None
            res.append(part)
        return res
        