/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    left  = 0 // buy
    right = 1 // sell
    profit = 0
    while (right < prices.length){
            if (prices[left] < prices[right]){
                currentProfit = prices[right] - prices[left] 
                if (currentProfit > profit){
                    profit = currentProfit
                }
            }else{
                left = right
            }
            right += 1
        }
        return profit
        
    
};
        

        