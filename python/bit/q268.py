#Bit manipulation
def missingNumber1(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    for i in range(0,len(nums)+1):
        ans ^= i
    for i in nums:
        ans ^= i
    return ans



#Math approach
def missingNumber2(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sum1 = (1+len(nums))*len(nums)/2
    sum2 = sum(nums)
    return sum1-sum2

#Interesting approach
def missingNumber3(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sum = 0
    for i,val in enumerate(nums):
        sum += (val-i)
    return len(nums) - sum
