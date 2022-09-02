'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
'''

def contain_duplicate(arr):
    if len(arr) <= 1:
        return None
    for i in range(len(arr)):
        if arr[i] in arr[i+1 : len(arr)]:
            return True
    return False

print(contain_duplicate([1,2,3]))