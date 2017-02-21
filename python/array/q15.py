def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ret = []
    if len(nums) <= 2:
        return ret

    nums.sort()
    p1 = 0

    while p1 < len(nums) - 2:
        n1 = nums[p1]
        p2 = p1 + 1
        p3 = len(nums)-1
        while p2 < p3:
            n2 = nums[p2]
            n3 = nums[p3]
            total = n1 + n2 + n3
            if total == 0:
                ret.append([n1,n2,n3])
                p2 += 1
                p3 -= 1
                while p2 < p3 and nums[p2] == nums[p2-1]:
                    p2 += 1
                while p2 < p3 and nums[p3] == nums[p3+1]:
                      p3 -= 1
            elif total < 0:
                p2 += 1
            else:
                p3 -= 1

        p1 += 1
        while p1 < len(nums)-2 and nums[p1] == nums[p1-1]:
            p1 += 1

    return ret
