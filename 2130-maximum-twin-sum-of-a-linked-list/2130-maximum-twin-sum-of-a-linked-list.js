/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {number}
 */
var pairSum = function(head) {
    let result = -10000000000000000000
    let slow = head
    let fast = head
        
    // Reach the middle of list
    while(fast.next.next != null){
        fast = fast.next.next
        slow = slow.next
    }
        
    // Reverse the right side of given list
    let current = slow.next
    let temp1 = null
    let temp2 = slow.next
        
    while(current != null){
        temp2 = current.next
        current.next = temp1
        temp1 = current
        current = temp2
    }
            
    current = head
        
    // Comparing the two halves of list
    while (temp1 != null){
        let twin_sum = current.val + temp1.val
        result = Math.max(result, twin_sum)
        current = current.next
        temp1 = temp1.next
    }
        
        
    return result
};