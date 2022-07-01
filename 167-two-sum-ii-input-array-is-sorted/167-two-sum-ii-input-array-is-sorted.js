/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    var left = 0
    var right = numbers.length - 1
    if (numbers.length == 2){return [1, 2]}
    while(left < right){
          if (numbers[left] + numbers[right] == target){
              return [left+1, right+1]
          }else{
              if(numbers[left] + numbers[right] < target){
                  left += 1
              }else{
                  right -= 1
              }
          }
        
          }
};