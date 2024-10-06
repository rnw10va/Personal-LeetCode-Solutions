# Problem Name: 104. Maximum Depth of Binary Tree
# Problem Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is not None:
            if root.left is None:
                left = 1
            else:
                left = self.maxDepth(root.left) + 1
            if root.right is None:
                right = 1
            else:
                right = self.maxDepth(root.right) + 1
            if left > right:
                return left
            else:
                return right
        else: 
            return 0 
