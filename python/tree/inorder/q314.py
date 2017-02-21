"""
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples:

Given binary tree [3,9,20,null,null,15,7],
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
return its vertical order traversal as:
[
  [9],
  [3,15],
  [20],
  [7]
]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        q = collections.deque([(root,0)])
        dic = collections.defaultdict(list)

        while len(q):
            node,pos = q.popleft()
            dic[pos].append(node.val)
            if node.left:
                q.append((node.left,pos-1))
            if node.right:
                q.append((node.right,pos+1))

        return [dic[i] for i in sorted(dic)]
