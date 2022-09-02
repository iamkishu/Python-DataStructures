'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
'''

from unittest import result


def product_arr(arr):

    n = len(arr)
    if n == 0:
        return None
    
    left = [0]*n
    right = [0]*n

    left[0] = 1
    right[n-1] = 1

    for i in range(1, n):
        left[i] = arr[i-1] * left[i-1]
        right[n-i-1] = right[n-i] * arr[n-i]
      
    return [right[i] * left[i] for i in range(n)]

print(product_arr([1,2,3,4]))
