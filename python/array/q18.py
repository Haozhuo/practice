def fourSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    nums.sort()
    ret = []
    if len(nums) < 4:
        return ret
    p1 = 0
    while p1 < len(nums)-3:
        n1 = nums[p1]
        p2 = p1 + 1
        while p2 < len(nums) - 2:
            n2 = nums[p2]
            p3 = p2 + 1
            p4 = len(nums)-1
            while p3 < p4:
                n3 = nums[p3]
                n4 = nums[p4]
                total = n1 + n2 + n3 + n4
                if total == target:
                    ret.append([n1,n2,n3,n4])
                    p3 += 1
                    while p3 < p4 and nums[p3] == nums[p3-1]:
                        p3 += 1
                    p4 -= 1
                    while p3 < p4 and nums[p4] == nums[p4+1]:
                        p4 -= 1
                elif total > target:
                    p4 -= 1
                else:
                    p3 += 1

            p2 += 1
            while p2 < p3 and nums[p2] == nums[p2-1]:
                p2 += 1

        p1 += 1
        while p1 < p2 and nums[p1] == nums[p1-1]:
            p1 += 1

    return ret
