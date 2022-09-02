'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

def two_sum(arr, target):
    if len(arr) < 2:
        return None
    for i in range(len(arr)):
        index1 = i
        rem = target - arr[index1]
        if rem in arr[index1 + 1 : len(arr)]:
            index2 = arr.index(rem, index1 + 1)
            return [index1, index2]
    return None   
    
print(two_sum( [2,7,11,4], 9))