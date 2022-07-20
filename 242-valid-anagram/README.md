<h2><a href="https://leetcode.com/problems/valid-anagram/">242. Valid Anagram</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given two strings <code style="user-select: auto;">s</code> and <code style="user-select: auto;">t</code>, return <code style="user-select: auto;">true</code> <em style="user-select: auto;">if</em> <code style="user-select: auto;">t</code> <em style="user-select: auto;">is an anagram of</em> <code style="user-select: auto;">s</code><em style="user-select: auto;">, and</em> <code style="user-select: auto;">false</code> <em style="user-select: auto;">otherwise</em>.</p>

<p style="user-select: auto;">An <strong style="user-select: auto;">Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "anagram", t = "nagaram"
<strong style="user-select: auto;">Output:</strong> true
</pre><p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "rat", t = "car"
<strong style="user-select: auto;">Output:</strong> false
</pre>
<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length, t.length &lt;= 5 * 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> and <code style="user-select: auto;">t</code> consist of lowercase English letters.</li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Follow up:</strong> What if the inputs contain Unicode characters? How would you adapt your solution to such a case?</p>
</div>
<hr>
<h2>My Solution Process:</h2>

#### INPUTS:
        - 2 Strings t and s

#### OUTPUTS:
        - True  ===>> if t is an anagram of s
        - False ====> if t is not an anagram of s

#### RULES:
        - s and t consist of lowercase English letters, so we don't care about letters format(lower case or upper case).
        - Length of t and s is greater than or equal to 1 ===>>> 1 <= s.length, t.length
        - An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using   all the original letters exactly once.

#### TEST/ EDGE CASES:
        - Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
        - Length of t and s is 1 ===>> s=['i'], t=['i'], return True || s=['i'], t=['a'], return False
        - Length of t and s is bigger than 1 ===>> s=['zaki'], t=['kzai'], return True || s=['zaki'], t=['zamp'], return False

#### Questions to Ask:
        - do we need to check input format!! No, let's assum that the input format is always a string format

#### APPROACH: 

- **First Solution**: Time complexity is **O(nlogn)** because of sorting operation with memory space **O(1)**

        - If sorted(t) == sorted(s):
            - Return True
        - Else:
            - Return False
            
- **Second Solution**: Time complexity is **O(n)** with memory space **O(n)** because of using hash Maps, So this is the **Optimal Solution**.
        
        - Inisializing empty 2 hashMaps ===>> t_hashMap, s_hashMap
        - Looping trough t string
            - If letter in t_hashMap
                - t_hashMap[letter] += 1
            - Else:
                - t_hashMap[letter] = 1
                
        - Looping trough s string
            - If letter in s_hashMap
                - s_hashMap[letter] += 1
            - Else:
                - s_hashMap[letter] = 1
        
        - If s_hashMap == t_hashMap
            - Return True
        - Else:
            - Return False

#### Resources:
- [Valid Anagram - Leetcode 242 - Python - NeetCode](https://www.youtube.com/watch?v=9UtInBqnCgA)
- Javascript soring a object !!!!!!!!!!!    
