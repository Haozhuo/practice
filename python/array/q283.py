"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    s = 0
    e = 0
    while(e < len(nums)):
        if nums[e] == 0:
            e += 1
        else:
            if nums[s] == 0:
                nums[s],nums[e] = nums[e],nums[s]
            s += 1
            e += 1
