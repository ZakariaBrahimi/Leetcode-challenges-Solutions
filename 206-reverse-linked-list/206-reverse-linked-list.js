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
var reverseList = function(head) {
    if (head == null || head.next == null){
        return head
    }
 
    let current = head
    let previous_node = null
    let next_node = head
        
    while (current != null){
        next_node = current.next
        current.next = previous_node
        previous_node = current
        current = next_node
    }
            
    return previous_node
};