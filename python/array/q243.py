"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

"""
def shortestDistance(self, words, word1, word2):
    """
    :type words: List[str]
    :type word1: str
    :type word2: str
    :rtype: int
    """
    pos1 = -1
    pos2 = -1
    diff = len(words)

    for i,val in enumerate(words):
        if val == word1:
            pos1 = i
        elif val == word2:
            pos2 = i
        if pos1 != -1 and pos2 != -1:
            diff = min(diff,abs(pos1-pos2))

    return diff
