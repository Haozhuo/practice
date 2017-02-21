"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""
#Smart way O(m+n)
def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if len(matrix) == 0:
        return False
    i = 0
    j = len(matrix[0]) - 1
    while i < len(matrix) and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            i += 1
        else:
            j -= 1

    return False

#O(mlogn) Divide and conquer
def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
        if len(matrix) == 1:
            return self.binary_search(matrix[0],target)

        result1 = self.searchMatrix(matrix[:len(matrix)/2],target)
        if result1:
            return True
        else:
            return self.searchMatrix(matrix[len(matrix)/2:],target)


    def binary_search(self,nums,target):
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return nums[0] == target
        s,e = 0,len(nums)-1

        while s <= e:
            mid = int((s+e)/2)
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                e = mid - 1
            else:
                s = mid + 1

        return False
