<h2><a href="https://leetcode.com/problems/valid-palindrome/">125. Valid Palindrome</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A phrase is a <strong style="user-select: auto;">palindrome</strong> if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.</p>

<p style="user-select: auto;">Given a string <code style="user-select: auto;">s</code>, return <code style="user-select: auto;">true</code><em style="user-select: auto;"> if it is a <strong style="user-select: auto;">palindrome</strong>, or </em><code style="user-select: auto;">false</code><em style="user-select: auto;"> otherwise</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "A man, a plan, a canal: Panama"
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> "amanaplanacanalpanama" is a palindrome.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "race a car"
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> "raceacar" is not a palindrome.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = " "
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 2 * 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> consists only of printable ASCII characters.</li>
</ul>
</div>
<hr>
<h2>My Solution Process:</h2>

#### INPUTS:
        - String s

#### OUTPUTS:
        - True  ===>> if the string s is palindrome
        - False ====>> if the string s is not palindrome

#### RULES:
        - A phrase is a palindrome if it reads the same forward and backward
        - Converting all uppercase letters into lowercase letters
        - Removing all non-alphanumeric characters(letters & numbers)
        - Lenght of the string s is greater than 0 ===>> 1 <= s.length
        - s Consists only of printable ASCII characters.

#### TEST/ EDGE CASES:
        - An empty string ===>> s = " ", return True
        - Normale phrase ===>> s = "race a car", return False
        - String contains both of non-alphanumeric characters & alphanumeric characters ===>> s = "A man, a plan, a canal: Panama", return True
        - The given string contains only alphanumeric characters ===> s = "aaa a aaa aa", True
        - The given string contains only non-alphanumeric characters ===> s = " ,; : !", return True

#### Questions to Ask:
        - Should we care about input validation! No (it's just my assumption)

#### APPROACH: 
        
        - Removing non-alphanumeric characters & concatinate the string together & Turn it to lower case [Helper Function]
        - new_s = helperFunc(string)
        - Initializing front & back pointers with 0 & (new_s.length - 1)
        - Looping through the new_s (stopt at front < back)
            - If new_s[front] == new_s[back]
                - front += 1 & back -= 1
            - Else:
                - Return False
        - Return True
        
- **Helper Function:**

        - Looping through the string
            - If char is not alphanumeric
                - string.remove(char)
        - Return string.lowercase

- In this solution I have used **two pointers pattern**, so the time of complexity of this solution is **O(n)** with memory space **O(1)**.
- I have written the **helper function** for **code readability**.   
#### Resources:
- [NOTES.md](https://github.com/ZakariaBrahimi/Leetcode-challenges-Solutions/blob/main/125-valid-palindrome/NOTES.md)
- [Python String replace()](https://www.programiz.com/python-programming/methods/string/replace)
- [How to delete a character from a string using Python - stackoverflow](https://stackoverflow.com/questions/3559559/how-to-delete-a-character-from-a-string-using-python)
- [Valid Palindrome - Leetcode 125 - Python - NeetCode](https://www.youtube.com/watch?v=jJXJ16kPFWg)
- [JavaScript String toLowerCase()](https://www.w3schools.com/jsref/jsref_tolowercase.asp)
- [How to remove all the non-alphanumeric characters from a string using JavaScript? - using regex](https://melvingeorge.me/blog/remove-all-non-alphanumeric-characters-string-javascript)
- [ASCII printable characters](https://www.ascii-code.com/)

