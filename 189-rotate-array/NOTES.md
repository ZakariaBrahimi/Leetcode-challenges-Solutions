we should make the operation `k%len(nums)` because of the value of **k** it could be **bigger** than the length of `nums` array
​
**Example:**
```
- nums = [1,2,3,4], k = 6
- k = k % len(nums) # k = 6%4=2 so I need to rotate the array only 2 times not 6(actual k)
- first rotate      ==>>  4,1,2,3
- second rotate ==>> 3,4,1,2
- third rotate ==>>     2,3,4,1
- forth rotate ==>>    1,2,3,4 ==>> the original order of array | after that is the needed rotation that we acheive it by doing the k%len(nums) operation without doing the last four rotations
- 5th rotate ==>>       4,1,2,3
- 6st rotate ==>>       3,4,1,2 ==>> and this is the result that we want to acheive
```