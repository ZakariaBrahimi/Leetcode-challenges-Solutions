/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
    if (root === null) return []
        let queue = [root]
        let result = []
        
        
        while (queue.length > 0){
            let level = []
            const queueLength = queue.length
            for(i=0; i<queueLength; i++){
                let current = queue.shift()
                if (current != null){
                    level.push(current.val)
                    if (current.left != null){
                        queue.push(current.left)
                    }
                        
                    if (current.right != null){
                        queue.push(current.right)
                    }
                        
                }
            }
            result.push(level)
        }                    
        return result
};