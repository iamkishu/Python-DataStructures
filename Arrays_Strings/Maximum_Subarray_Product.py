'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
A subarray is a contiguous subsequence of the array.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
'''

def max_subarray_prod(arr):
    maxi, mini, max_prod = 1, 1, 0
    for i in  arr:
        if i < 0:
            maxi, mini = mini, maxi
        maxi = max(i, maxi*i)
        mini = min(i, mini*i)
        if max_prod < maxi:
            max_prod = maxi
    return max_prod

print(max_subarray_prod([-2,-3,-4,]))