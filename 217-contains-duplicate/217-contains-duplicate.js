/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    hashMap = {}
    for (let i=0; i<nums.length; i++){
        if (nums[i] in hashMap){
            return true
        }else{
            hashMap[nums[i]] = 1
        }
    }
    return false
};