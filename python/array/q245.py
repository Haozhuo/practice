"""
This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
You may assume word1 and word2 are both in the list.
"""
#faster
def shortestWordDistance(self, words, word1, word2):
    """
    :type words: List[str]
    :type word1: str
    :type word2: str
    :rtype: int
    """
    i1 = len(words)
    i2 = -i1
    diff = len(words)
    same = word1==word2
    for i,val in enumerate(words):
        if val == word1:
            i1 = i
            if same:
                i1,i2 = i2,i1
        elif val == word2:
            i2 = i

        diff = min(abs(i1-i2),diff)
    return diff
#shorter
def shortestWordDistance(self, words, word1, word2):
    """
    :type words: List[str]
    :type word1: str
    :type word2: str
    :rtype: int
    """
    i1 = len(words)
    i2 = -i1
    diff = len(words)
    for i,val in enumerate(words):
        if val == word1:
            i1 = i
        if val == word2:
            if word1 == word2:
                i1 = i2
            i2 = i

        diff = min(abs(i1-i2),diff)
    return diff
