import collections
def fourSumCount1(self, A, B, C, D):
    """
    :type A: List[int]
    :type B: List[int]
    :type C: List[int]
    :type D: List[int]
    :rtype: int
    """
    """
    counter: count the number of appearance of an element
    in an iterable; when key does not exists, it will return 0 as
    it's value as opposed to dict which will raise a key error
    """
    dic = collections.Counter([a+b for a in A for b in B])
    return sum([dic[-c-d] for c in C for d in D])

def fourSumCount(self, A, B, C, D):
    """
    :type A: List[int]
    :type B: List[int]
    :type C: List[int]
    :type D: List[int]
    :rtype: int
    """
    dic = {}
    for a in A:
        for b in B:
            dic[a+b] = dic.get(a+b,0) + 1
    return sum(dic.setdefault(-c-d,0) for c in C for d in D)
