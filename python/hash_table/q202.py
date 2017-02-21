"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""
def isHappy1(self, n):
    """
    :type n: int
    :rtype: bool
    """
    mem = []
    while n != 1:
        n = sum([int(n)**2 for val in str(n)])
        if n in mem:
            return False
        else:
            mem.append(n)

    return True

def isHappy2(self, n):
    """
    :type n: int
    :rtype: bool
    """
    #Fast and slow pointers
    slow = n
    fast = n
    while True:
        slow = sum([int(val)**2 for val in str(slow)])
        fast = sum([int(val)**2 for val in str(fast)])
        fast = sum([int(val)**2 for val in str(fast)])
        if fast == slow:
            break

    if slow != 1:
        return False
    return True
