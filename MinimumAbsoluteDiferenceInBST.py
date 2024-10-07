# Problem Name: 530. Minimum Absolute Difference in BST
# Problem Link: https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ints = self.getArray(root)
        minDif = ints[1]-ints[0]
        for i in range(2,len(ints)):
            minDif = min(minDif, ints[i]-ints[i-1])
        return minDif

    def getArray(self, root):
        arrayToReturn = []
        if root.left is not None:
            arrayToReturn.extend(self.getArray(root.left))
        arrayToReturn.append(root.val)
        if root.right is not None:
            arrayToReturn.extend(self.getArray(root.right))
        return arrayToReturn
                
