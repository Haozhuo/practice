"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
"""
def diffWaysToCompute(self, input):
    """
    :type input: str
    :rtype: List[int]
    """
    if input.isdigit():
        return [int(input)]

    ret = []
    for i,val in enumerate(input):
        if val in "+-*":
            res1 = self.diffWaysToCompute(input[:i])
            res2 = self.diffWaysToCompute(input[i+1:])

            for val1 in res1:
                for val2 in res2:
                    if val == '+':
                        ret.append(val1+val2)
                    elif val == '-':
                        ret.append(val1-val2)
                    else:
                        ret.append(val1*val2)

    return ret
