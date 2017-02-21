"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
"""
def isStrobogrammatic(self, num):
    """
    :type num: str
    :rtype: bool
    """
    dic = {}
    dic["0"],dic["1"],dic["6"],dic["8"],dic["9"] = "0","1","9","8","6"
    s, e = 0, len(num) - 1
    while s <= e:
        if num[s] not in dic or dic[num[s]] != num[e]:
            return False
        s += 1
        e -= 1

    return True
