"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
"""
def containsNearbyDuplicate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    dic = {}
    for i,val in enumerate(nums):
        if val in dic:
            if i - dic[val] <= k:
                return True
            else:
                dic[val] = i
        else:
            dic[val] = i

    return False
