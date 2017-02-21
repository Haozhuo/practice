"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""
#Normal DP
def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    ret = [0]*len(nums)
    ret[0] = nums[0]
    max_val = nums[0]

    for i in range(1,len(nums)):
        ret[i] = max(ret[i-1]+nums[i],nums[i])
        max_val = max(max_val,ret[i])

    return max_val

#Simplified DP
def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0

    res = float("-inf")
    sum = 0

    for i in range(0,len(nums)):
        sum = max(0,sum) + nums[i]
        res = max(res,sum)

    return res
