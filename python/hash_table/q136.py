"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    for num in nums:
        ans ^= num
    return ans
