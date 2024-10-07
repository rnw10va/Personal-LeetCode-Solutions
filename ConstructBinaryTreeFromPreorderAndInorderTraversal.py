# Problem Name: 105. Construct Binary Tree from Preorder and Inorder Traversal
# Problem Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
