def frequencySort(self, s):
    """
    :type s: str
    :rtype: str
    """
    return "".join([c * times for c, times in collections.Counter(s).most_common()])
