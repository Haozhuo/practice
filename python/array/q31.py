def nextPermutation(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    i = len(nums) - 1
    while i > 0:
        if nums[i] > nums[i-1]:
            j = len(nums)-1
            while j > i-1:
                if nums[j] > nums[i-1]:
                    nums[i-1], nums[j] = nums[j],nums[i-1]
                    break
                j -= 1
            nums[i:len(nums)] = nums[len(nums)-1:i-1:-1]
            break
        i-=1

    if i == 0:
        nums.reverse()
