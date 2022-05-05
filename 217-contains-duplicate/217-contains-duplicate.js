/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    hashSet = new Set()
    for (let i=0; i<nums.length; i++){
        if (hashSet.has(nums[i])){
            return true
        }
        hashSet.add(nums[i])
    }
    return false
};