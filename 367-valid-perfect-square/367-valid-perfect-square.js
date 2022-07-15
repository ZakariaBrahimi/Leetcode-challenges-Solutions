/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function(num) {
    let left = 1
    let right = num
    let middle = 0
    
    while (left <= right){
        middle = Math.floor((left + right) / 2)
        if (middle*middle == num){
            return true
        }else{
            if (middle*middle < num){
                left = middle + 1
            }else{
                right = middle - 1
            }
                
            }
    }
    return false
};