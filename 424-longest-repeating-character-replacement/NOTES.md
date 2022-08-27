* To simplify it and make the code more efficient:
```python
class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    count = {}
    res = 0
​
    l = 0
    maxf = 0
    for r in range(len(s)):
      count[s[r]] = 1 + count.get(s[r], 0)
      maxf = max(maxf, count[s[r]]) # the logic here is simple, just walk through it with some examples
      # keep shifting the left pointer if the sub-string is not valid
      while (r - l + 1) - maxf > k:
        count[s[l]] -= 1
        l += 1
      # the last while loop give us a valid sub-string -> so take the length of it.
    res = max(res, r - l + 1)
    return res
```

#### Resources:
- [how to solve any sliding window technique](https://labuladong.gitbook.io/algo-en/iii.-algorithmic-thinking/slidingwindowtechnique)
- [Longest Repeating Character Replacement - Leetcode 424 - Python](https://www.youtube.com/watch?v=gqXU1UyA8pk)
