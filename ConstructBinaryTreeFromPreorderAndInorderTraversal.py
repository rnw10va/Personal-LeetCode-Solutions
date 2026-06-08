"""
Problem Name: 105. Construct Binary Tree from Preorder and Inorder Traversal
# Problem Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
Problem Description:
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.


Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]


Constraints:
    1 <= preorder.length <= 3000
    inorder.length == preorder.length
    -3000 <= preorder[i], inorder[i] <= 3000
    preorder and inorder consist of unique values.
    Each value of inorder also appears in preorder.
    preorder is guaranteed to be the preorder traversal of the tree.
    inorder is guaranteed to be the inorder traversal of the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#My Solution
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        i = 0
        root = TreeNode()
        while inorder[i] != preorder[0]:
            i+=1
        root.val = preorder[0]
        if i > 0:
            root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        if i + 1 < len(preorder):
            root.right = self.buildTree(preorder[i+1:], inorder[i + 1:])
        return root