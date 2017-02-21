"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
"""
def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    while(m > 0 and n > 0):
        if nums1[m-1] > nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
        else:
            nums1[m+n-1] = nums2[n-1]

    if n > 0:
        nums1[:n] = nums2[:n]




def merge2(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    i1 = m - 1
    i2 = n - 1
    for i in range(m+n-1,-1,-1):
        if i2 < 0:
            break
        if i1 < 0:
            for j in range(0,i+1):
                nums1[j] = nums2[j]
            break
        if nums1[i1] > nums2[i2]:
            nums1[i] = nums1[i1]
            i1 -= 1
        else:
            nums1[i] = nums2[i2]
            i2 -= 1
