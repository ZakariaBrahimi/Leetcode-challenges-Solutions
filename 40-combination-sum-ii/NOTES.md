#### Complexity Analysis
​
##### Let N be the size of the input array.
​
##### Time Complexity: O(2^N)
​
* **In the worst case**, our algorithm will exhaust all possible combinations from the input array, which in total amounts to 2^N as we discussed before.
​
* **The sorting** will take \mathcal O(N log N).
​
* **To sum up**, the overall time complexity of the algorithm is dominated by the backtracking process, which is \mathcal O(2^N)
​
##### Space Complexity: O(N)
​
* We use the variable comb to keep track of the current combination we build, which requires \mathcal{O}(N)O(N) space.
​
* **In addition**, we apply recursion in the algorithm, which will incur additional memory consumption in the function call stack. In the worst case, the stack will pile up to O(N) space.
* **To sum up**, the overall space complexity of the algorithm is O(N) +  O(N) =O(N).
​
**Note:** we did not take into account the space needed to hold the final results of combination in the above analysis.