"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""
#Method1
def majorityElement1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dic = {}
    for val in nums:
        if val in dic:
            dic[val] += 1
        else:
            dic[val] = 1
        if(dic[val]) > int(len(nums)/2):
            return val

//# NOTE: Better way
#Method2
def majorityElement2(nums):
    majority = 0
    count = 0
    for i in range(0,len(nums)):
        if not count:
            count = 1
            majority = nums[i]
        else:
            if majority == nums[i]:
                count += 1
            else:
                count -= 1

    return majority
