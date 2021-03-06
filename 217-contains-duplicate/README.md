<h2><a href="https://leetcode.com/problems/contains-duplicate/">217. Contains Duplicate</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an integer array <code style="user-select: auto;">nums</code>, return <code style="user-select: auto;">true</code> if any value appears <strong style="user-select: auto;">at least twice</strong> in the array, and return <code style="user-select: auto;">false</code> if every element is distinct.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,2,3,1]
<strong style="user-select: auto;">Output:</strong> true
</pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,2,3,4]
<strong style="user-select: auto;">Output:</strong> false
</pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,1,1,3,3,4,3,2,4,2]
<strong style="user-select: auto;">Output:</strong> true
</pre>
<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">9</sup> &lt;= nums[i] &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
</ul>
</div>

<hr/>
<h2>My Solution Process</h2>

#### INPUTS:
        - Array of integer values _nums_

#### OUTPUTS:
        - True  ===>> if there are two duplicats elements in the array
        - False ===>> if there are not duplicats elements in the array

#### RULES:
        - Length of array is greater than or equal to 1 ===>> 1 <= nums.length <= 10_5
        - The given array may contains negitative values ===>> -10_9 <= nums[i] <= 10_9

#### EDGE/ TEST CASES:
        - Array of length 1 ===>> [1], return False
        - All array elements are positive ===>> [1,1,1,3,3,4,3,2,4,2], return True
        - All array elements are negative ===>> [-1,-2,-3,-1], return True
        - The given array contains both of negative & positive elements ===>> [1,2,-5,7,-9], return False




#### APPROACH:
- The **brute force solution** if using **2 nested for loops** which means two pointers, but here the time complexity is **O(n2)** which is not efficient, and the space complexity is O(1)
- The **second solution** is by **sorting the given array**, the time complexity of this is **O(nlog)** which is more efficient than O(n2) (nlogn because of the sorting operation), and the space complexity is **O(1)**.
        
        - Initialize an empty hashSet
        - Looping through the given array.
            - If item in hashSet
                - Return True
            - Else:
                - Add each item of array in that hashSet
        - Return False
        
- but by using a **hashMap**, the time complexity will be **decrease** to **O(n)**, which is more efficient than **O(n2)** and **O(nlogn)**, but hashSet need more **memory space** which is **O(n)** (because it could takes the size of the given array) .
#### Resources:
- [Contains Duplicate - Leetcode 217 - Python - NeetCode](https://www.youtube.com/watch?v=3OamzN90kPg)
- [JavaScript hash Sets](https://www.w3schools.com/js/js_object_sets.asp)
- [Contains Duplicate | Coding Interview Question and Answer Study Guide](https://www.youtube.com/watch?v=kbF5x_K95Jg&list=PL53JxaGwWUqA1i2fcKXTGkDi9nr0QCAaz&index=2)
