"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""
#divide and conquer
def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        return self.helper(nums,0,len(nums)-1)

    def helper(self,nums,l,r):
        if l == r:
            return nums[l]
        if l > r:
            return float("-inf")

        m = int((l+r)/2)
        leftMax = rightMax = 0
        sum_num = 0
        for i in range(m-1,l-1,-1):
            sum_num += nums[i]
            leftMax = max(sum_num,leftMax)

        sum_num = 0
        for i in range(m+1,r+1):
            sum_num += nums[i]
            rightMax = max(sum_num,rightMax)

        ans1 = self.helper(nums,l,m-1)
        ans2 = self.helper(nums,m+1,r)

        return max(max(ans1,ans2),leftMax+nums[m]+rightMax)

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
    sum_val = 0

    for i in range(0,len(nums)):
        sum_val = max(0,sum) + nums[i]
        res = max(res,sum_val)

    return res
