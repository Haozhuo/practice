"""
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""
def summaryRanges(self, nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    ret = []
    s = e = 0
    print_func = lambda s,e: str(s) + "->" + str(e) if s != e else str(e)
    for i in range(1,len(nums)+1):
        if i == len(nums) or nums[i] - nums[i - 1] != 1:
            e = i - 1
            ret.append(print_func(nums[s],nums[e]))
            s = i

    return ret
