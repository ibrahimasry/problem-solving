/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {ListNode} head
 * @return {TreeNode}
 */
var sortedListToBST = function(head) {
    let curr = head
    let length = 0
    while(head) head = head.next, length++
    const helper = (start , end)=>{
        if(start >= end) return null
        const mid = Math.floor( (start + end) / 2)
        const left = helper(start, mid)
        const val = curr.val
        curr = curr.next
        return  new TreeNode(val, left , helper(mid + 1, end))        
    }
   return helper(0, length)
};