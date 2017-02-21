"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) <= 1:
            return nums[0]
        #第number大的数字
        index = self.reorder(nums[0],nums)
        number = len(nums) - index

        if number == k:
            return nums[index]
        elif number < k:
            return self.findKthLargest(nums[:index],k-number)
        else:
            return self.findKthLargest(nums[index+1:],k)


    def reorder(self,pivot,nums):
        """
        pivot:int
        nums:List[int]
        rtype: int
        """
        s,e = 1,len(nums) - 1
        while s < e:
            if nums[s] > pivot and nums[e] <= pivot:
                nums[s],nums[e] = nums[e],nums[s]
                s += 1
                e -= 1
            elif nums[s] <= pivot:
                s += 1
            elif nums[e] > pivot:
                e -= 1

        if nums[s] <= pivot:
            nums[s],nums[0] = nums[0],nums[s]
            return s
        else:
            nums[s-1],nums[0] = nums[0],nums[s-1]
            return s-1
