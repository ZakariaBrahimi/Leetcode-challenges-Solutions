/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteMiddle = function(head) {
    if ( !head.next){
        return null
    }
        
    let slow = head
    let fast = head
    let temp = null
        
    while (fast && fast.next){
        temp = slow
        fast = fast.next.next
        slow = slow.next
    }
   
    temp.next = slow.next
    slow.next = null
    
    return head
};