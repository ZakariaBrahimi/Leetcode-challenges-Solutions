
var twoSum = function(nums, target) {
    let hashMap = {};
    if (nums.length == 2){ return [0, 1]}
    for (let i = 0; i < nums.length; i++) {
        let RequiredVal = target - nums[i];
        if (RequiredVal in hashMap) {
            return [hashMap[RequiredVal], i];
        }
        hashMap[nums[i]] = i;

    }
};