# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash = defaultdict()
        
        
        dummy = ListNode()
        hash[0] = dummy
        dummy.next = head
        curr = dummy.next
        pre = 0
        while curr:
            pre += curr.val
            if pre in hash :
                currNode= hash[pre].next
                start = currNode.val + pre
                while start != pre:
                    currNode = hash[start].next                    
                    del hash[start]
                    start += currNode.val
                hash[start].next = curr.next
            else :
                hash[pre] = curr

            curr = curr.next
        return dummy.next
                
            