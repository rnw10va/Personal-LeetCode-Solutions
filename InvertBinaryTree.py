# Problem Name: 226. InvertBinaryTree
# Problem Link: https://leetcode.com/problems/invert-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        else:
            temp = self.invertTree(root.left)
            root.left = self.invertTree(root.right)
            root.right = temp
            return root
