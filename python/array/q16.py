def threeSumClosest(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    ans = float("inf")
    ret = 0

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
            if total == target:
                ans = 0
                ret = total
                return total
            elif total < target:
                if ans > abs(target-total):
                    ans = abs(target-total)
                    ret = total
                p2 += 1
            else:
                print(ans,abs(target-total))
                if ans > abs(target-total):
                    ans = abs(target-total)
                    ret = total
                print(ret)
                print("-"*10)
                p3 -= 1
        p1 += 1
    return ret
