/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
   let maxArea= 0;
   let left= 0;
   let right = height.length-1;
    // we will keep moving till we cross the right
    while(left<right){
        let width= right-left;
        let minHeight= Math.min(height[left],height[right]);
        maxArea = Math.max(maxArea,(width*minHeight));
        
        // the logic is we will keep going closer to the max height either from left or right
        if(height[left]<height[right]){
            left++;
        }else{
            right--;
        }
    }
    return maxArea;
};
