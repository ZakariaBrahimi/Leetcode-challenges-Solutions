<h2><a href="https://leetcode.com/problems/two-sum/">1. Two Sum</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an array of integers <code style="user-select: auto;">nums</code>&nbsp;and an integer <code style="user-select: auto;">target</code>, return <em style="user-select: auto;">indices of the two numbers such that they add up to <code style="user-select: auto;">target</code></em>.</p>

<p style="user-select: auto;">You may assume that each input would have <strong style="user-select: auto;"><em style="user-select: auto;">exactly</em> one solution</strong>, and you may not use the <em style="user-select: auto;">same</em> element twice.</p>

<p style="user-select: auto;">You can return the answer in any order.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [2,7,11,15], target = 9
<strong style="user-select: auto;">Output:</strong> [0,1]
<strong style="user-select: auto;">Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [3,2,4], target = 6
<strong style="user-select: auto;">Output:</strong> [1,2]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [3,3], target = 6
<strong style="user-select: auto;">Output:</strong> [0,1]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">2 &lt;= nums.length &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">9</sup> &lt;= nums[i] &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">9</sup> &lt;= target &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
	<li style="user-select: auto;"><strong style="user-select: auto;">Only one valid answer exists.</strong></li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<strong style="user-select: auto;">Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than&nbsp;<code style="user-select: auto;">O(n<sup style="user-select: auto;">2</sup>)&nbsp;</code>time complexity?</div>

<hr/>
<h2>My Solution Process</h2>


#### INPUTS:
        - Array of integers _nums_
        - Integer target _target_

#### OUTPUTS:
        - Array of two indices of two numbers that they add up to target 
          ===>> nums[i] + nums[j] = target

#### RULES:
        - Each input have exactly one solution.
        - Don't use the same element twice.
        - Returning the answer in any order.
        - Length of the array is greater than 2 ===>> 2 <= nums.length <= 10_4
        - Elements of the array could be positive and nigative integer ===>> -10_9 <= nums[i] <= 10_9
        - The target value could be positive and nigative integer ===>> -10_9 <= target <= 10_9


#### EDGE/ TEST CASES:
        - Array of length 2 ===>> [3,3] target = 6, return [0, 1]
        - Array contains only positive integers && Target value is positive  [1,4,3,8], target = 12, return [1, 3]  
        - Array contains only nigative integers && Target value is nigative  [-21,-7,-3,-2], target = -5, return [2, 3]
        - Array contains nigative and positive integers && Target value is nigative  [-21,7,-3,2], target = -14, return [0, 1]
        - Array contains nigative and positive integers && Target value is positive  [-21,7,-3,2], target = 4, return [1, 2]

#### Questions to Ask:
        - Is the array sorted ! No (just Assumption)
        - Should I make input validation ! No (just Assumption)

#### APPROACH:       
- The first Solution come up to my mind (brute force solution) is using 2 nested for loops
but here the time complexity is going to be O(n2) which is not the optimal solution.

        - Initialize an empty hashMap. {arrElemnt: itsIndice}
        - Looping through the array one by one
           - RequiredVal = target - curItem
           - If requiredVal is in hashMap
              - Return hashMap[requiredVal], currentIndex[curItem]
           - Else:
              - hashMap[curItem] = current item indice
- By using hash maps, the time complexity will be O(n), which is more efficient than O(n2).
#### Resources: 
- [Two Sum - Leetcode #1 Short & Simple Solution](https://www.code-recipe.com/post/two-sum)
- [[Python] List approach O(n²) - (2620ms) and Dictionary approach O(n) - (62ms)
](https://leetcode.com/problems/two-sum/discuss/1999084/Python-List-approach-O(n)-(2620ms)-and-Dictionary-approach-O(n)-(62ms))
- [Python enumerate() method](https://www.programiz.com/python-programming/methods/built-in/enumerate)
- [Two Sum - Leetcode 1 - HashMap - Python - NeetCode](https://www.youtube.com/watch?v=KLlXCFG5TnA&t=7s)
- [Why is Tuple faster than List and when to use List
](https://medium.com/@prajeen.v/why-tuples-are-faster-and-when-to-use-list-f2f07291e923)
