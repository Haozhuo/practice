"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""
def thirdMax(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    top3 = [float("-inf"),float("-inf"),float("-inf")]
    for val in nums:
        if val > top3[0]:
            top3 = [val,top3[0],top3[1]]
        elif val < top3[0] and val > top3[1]:
            top3 = [top3[0],val,top3[1]]
        elif val < top3[1] and val > top3[2]:
            top3 = [top3[0],top3[1],val]

    if top3[2] == float("-inf"):
        return top3[0]
    else:
        return top3[2]
