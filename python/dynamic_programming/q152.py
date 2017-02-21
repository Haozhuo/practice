def maxProduct(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums)==0:
        return 0;
    r = imax = imin = nums[0]
    for val in nums[1:]:
        if val < 0:
            imax,imin = imin,imax
        imax = max(val,val*imax)
        imin = min(val,val*imin)
        r = max(r,imax)
    return r
