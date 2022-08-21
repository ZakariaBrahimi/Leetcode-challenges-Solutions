/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    memo = {}
    return memoization(n)
};
var memoization = (n)=>{
    if (n in memo) return memo[n]
    if (n == 0) return 1
    if (n == -1) return 0
    memo[n] = memoization(n-1) + memoization(n-2)
    return memo[n]
}