# Problem Name: 114. Flatten Binary Tree to Linked List
# Problem Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        elif root.left is not None:
            self.flatten(root.left)
            if root.right is not None:
                self.flatten(root.right)
                temp=root.right
                root.right=root.left
                root.left=None
                temp2=root.right
                while temp2.right is not None:
                    temp2=temp2.right
                temp2.right=temp
            else:
                self.flatten(root.right)
                root.right=root.left
                root.left=None
        else:
            self.flatten(root.right)
