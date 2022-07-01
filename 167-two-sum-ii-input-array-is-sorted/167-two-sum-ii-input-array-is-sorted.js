	/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    if(numbers.length == 2){
        return [1, 2]
    }
    leftPointer = 0 
    rightPointer = numbers.length - 1
    while (leftPointer < rightPointer){
        sum = numbers[leftPointer] + numbers[rightPointer]
        if (sum == target){
                return [leftPointer+1, rightPointer+1]
        }else{
            if(sum < target){
                leftPointer += 1
            }else{
                rightPointer -= 1
            }
            
        }
    }
};