"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
"""
# NOTE: Cyclic replacement

def rotate2(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    temp =  nums[len(nums)-k:] + nums[:len(nums)-k]
    for i,val in enumerate(temp):
        nums[i] = val


def rotate3(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    nums.reverse()
    nums[:k] = list(reversed(nums[:k]))
    nums[k:] = list(reversed(nums[k:]))
