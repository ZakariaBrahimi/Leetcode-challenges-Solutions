/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    let count = 0 
    let result = 0       
    let right = 0
    while(right < nums.length){
        if (nums[right] == 0) {
            result = Math.max(result, count)
            right += 1
            count = 0
        }else{
            count += 1
            right += 1
        }                   
        if (right == nums.length){
            result = Math.max(result, count)
        }
            
                
    }
        
        return result
};