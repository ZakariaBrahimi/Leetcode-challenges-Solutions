var longestOnes = function(nums, k) {
    let left = 0
    let right = 0
    let result = 0
    let zero_counter = 0
    while (right<nums.length){
        if (nums[right] == 0){
            zero_counter += 1
        }       
        while(zero_counter > k){
            if (nums[left] == 0){
                zero_counter -= 1
            }     
            left += 1
        }
        result = Math.max(result, right-left+1)
        right += 1
    }    
    return result      
        
};