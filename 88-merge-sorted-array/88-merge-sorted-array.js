/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    let p1 = m-1
    let p2 = n-1
    let last = m+n-1
    while (p2 +1> 0 && p1 +1> 0){
        if (nums1[p1] < nums2[p2]){
            nums1[last] = nums2[p2]
            p2 -= 1
        }else{
            nums1[last] = nums1[p1]
            p1 -= 1
        }
        last -= 1
        
    }
    while (p2+1 >0){
        nums1[last] = nums2[p2]
        p2 -= 1
        last -= 1
    }
    return nums1
};


        
        
        