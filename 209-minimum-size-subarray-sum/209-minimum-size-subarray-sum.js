/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    let left = 0
    let result = 1000000000
    let current_sum = 0 
        
    for (let right=0; right<nums.length; right++){
        current_sum += nums[right]
        while (current_sum >= target){
            result = Math.min(result, right-left+1)
            current_sum -= nums[left]
            left += 1
        }
    }
        return (result != 1000000000) ? result  : 0
};