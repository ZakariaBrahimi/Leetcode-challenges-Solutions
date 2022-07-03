/**
 * @param {number[]} nums
 * @return {number[]}
 */       
var productExceptSelf = function(nums) {
    let result = [1]
    let prod = 1
    for(i=1; i<nums.length; i++){
        prod *= nums[i-1]
        result.push(prod)
    }
    prod = 1
    for(i=nums.length-1; i>-1; i--){
        if (i==nums.length-1){continue}
        prod = prod*nums[i+1]
        result[i] = result[i]*prod
    }
    return result
};