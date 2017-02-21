"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
"""
def minSubArrayLen(self, s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    total,start,min_len=0,0,len(nums)+1
    for i in range(0,len(nums)):
        total += nums[i]
        while total >= s:
            min_len = min(min_len,i-start+1)
            total -= nums[start]
            start += 1

    if min_len == len(nums)+1:
        return 0
    else:
        return min_len
