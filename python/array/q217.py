"""
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""
def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    dic = {}
    for val in nums:
        if val in dic:
            return True
        else:
            dic[val] = 1
    return False
