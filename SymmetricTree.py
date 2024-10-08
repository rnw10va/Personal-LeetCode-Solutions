# Problem Name: 101. Symmetric Tree
# Problem Link: https://leetcode.com/problems/symmetric-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.compareTrees(root.left, root.right)

    def compareTrees(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is not None and root2 is not None:
            return root1.val == root2.val and self.compareTrees(root1.right, root2.left) and self.compareTrees(root1.left, root2.right)
        else:
            return False 
