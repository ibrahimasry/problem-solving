/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    
    let dummy = new ListNode()
    let head = dummy
    let carry = 0
    while(l1 || l2 || carry){
        let v1 = l1?.val || 0
        let v2 = l2?.val || 0
        
        let currSum = v1 + v2 +carry
        
        head.next = new ListNode(currSum % 10)
        head = head.next
        carry = Math.floor(currSum / 10)
        l1 = l1 && l1.next
        l2 = l2 && l2.next
    }
    
    
    return dummy.next
    
    
    
};