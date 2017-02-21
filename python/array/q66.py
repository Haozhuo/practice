"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

"""
# NOTE: Better approach
def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    num = 0
    for i in range(0,len(digits)):
        num += pow(10,len(digits)-1-i)
    return [int(i) for i in str(num+1)]

def plusOne2(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    ret = digits[::-1]
    carry = 1
    for i in range(0,len(digits)):
        ret[i] += carry
        if ret[i] >= 10:
            ret[i] -= carry * 10
            carry = 1
        else:
            carry = 0

    if carry == 1:
        ret.append(1)

    return ret[::-1]
