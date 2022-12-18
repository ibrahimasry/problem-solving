# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        curr = curr.next
        l = 0
        while curr:
            curr = curr.next 
            l += 1
        first = dummy
        i = 0
        while i < k:
            first = first.next
            i+=1
        i = l - k +1
        second = dummy
        
        while i:
            second = second.next
            i -= 1
        second.val , first.val = first.val, second.val
        return dummy.next