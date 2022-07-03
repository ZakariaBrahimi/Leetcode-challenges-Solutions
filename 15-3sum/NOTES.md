* **There is a interesting trick here, revise it later.**
* First of all,we need to sort the given array **
* and then I **fix a target** value and then initialize the **two pointers** (in the beginning and the end indices
* Shift those two pointers togather until both meet
* if fixed target value(a) + value of two pointers(nums[p1]+nums[p2]) are bigger than 0
* Decrement the second pointer by 1
* if fixed target value(a) + value of two pointers(nums[p1]+nums[p2]) are less than 0
* Increment the first pointer by 1
* if fixed target value(a) + value of two pointers(nums[p1]+nums[p2]) are equal to 0
*   Increment the first pointer by 1
*   and then check if the next item is the same asthe previous one
*   if it is: then increament it again until we find different value
​