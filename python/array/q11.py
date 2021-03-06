"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""
def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    s,e,max_area = 0,len(height)-1,0

    while s < e:
        max_area = max(max_area,min(height[s],height[e])*(e-s))
        if height[s] <= height[e]:
            s += 1
        else:
            e -= 1

    return max_area
