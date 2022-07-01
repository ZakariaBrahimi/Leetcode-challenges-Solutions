/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */

var reverse = (nums, start, end)=>{
        start = start
        end = end
        let temp = 0
        while (start < end){
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
        }
};
var rotate = function(nums, k) {
    k = k % nums.length
    if (nums.length == 1 || k == 0){return nums};
    reverse(nums, 0, nums.length - 1)
    reverse(nums, start=0, end=k-1)
    reverse(nums, start=k, end=nums.length-1)
    return nums
};