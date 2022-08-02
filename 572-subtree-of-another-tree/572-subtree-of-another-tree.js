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
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function(root, subRoot) {
    if  (subRoot === null) return true
    if (root === null)return false

    if (isSame(root, subRoot)) return true
    if (!isSame(root, subRoot)){
        let left = isSubtree(root.left, subRoot)
        let right = isSubtree(root.right, subRoot)
        return left || right
    }
            
};
  
var isSame = (root, subRoot)=>{
    if (root === null && subRoot === null) return true
    if (root && subRoot && root.val == subRoot.val){
        let left = isSame(root.left, subRoot.left)
        let right = isSame(root.right, subRoot.right)
        return left && right
    }else{ return false }
}
        
            
        