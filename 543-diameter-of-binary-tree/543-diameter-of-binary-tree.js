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
 * @return {number}
 */
var diameterOfBinaryTree = function(root) {
    return dfs(root)[1]
};

var dfs = (root) =>{
    if (root === null) return [0, 0] // [hight, diameter]
    
    let left             = dfs(root.left)
    let right            = dfs(root.right)
    let longest_diameter = Math.max(left[1], right[1], left[0] + right[0])
        
    return [1 + Math.max(left[0], right[0]), longest_diameter]
}      