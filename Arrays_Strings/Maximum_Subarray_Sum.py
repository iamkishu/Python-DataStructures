'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

######## kaden's algo ##########
def max_subarray_sum(arr):
    curr_sum = 0
    max_sum = 0
    for i in arr:
        curr_sum += i
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    if max_sum == 0:
        max_sum = min(arr)
    return max_sum

print(max_subarray_sum([-1, -4, -2, -3]))