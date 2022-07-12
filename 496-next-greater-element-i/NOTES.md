* It's really hard question for the first time
### Brute force solution:
```python
nums1_hash_map = {value:index for index, value in enumerate(nums1) }
result = [-1] * len(nums1)
for i in range(len(nums2)):
if nums2[i] in nums1_hash_map:
for j in range(i+1, len(nums2)):
if nums2[i] < nums2[j]:
index = nums1_hash_map[nums2[i]]
value = nums2[j]
result[index] = value
break
return result
```
​