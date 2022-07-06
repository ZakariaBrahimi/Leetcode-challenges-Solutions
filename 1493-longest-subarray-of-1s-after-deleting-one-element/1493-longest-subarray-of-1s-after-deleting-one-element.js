var longestSubarray = function(nums) {
   let result = 0
    let left = 0
    let ziro_counter = 0
        
    for(let right=0; right<nums.length; right++){
        if (nums[right] == 0){
            ziro_counter += 1
        }    
            while( ziro_counter > 1){
                if (nums[left] == 0){
                    ziro_counter -= 1
                }   
                left += 1
            }
            result = Math.max(result, right - left)
    }
                  
        return result 
};