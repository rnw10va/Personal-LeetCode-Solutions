# Problem Name: 88. Merge Sorted Array
# Problem Link: https://leetcode.com/problems/merge-sorted-array/description/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = 0
        j = 0
        while i < m + j and j < n:
            if nums1[i] >= nums2[j]:
                nums1.insert(i,nums2[j])
                nums1.pop()
                i+=1
                j+=1
            else:
                i+=1
        if j < n:
            for k in range(j,n):
                nums1.insert(i,nums2[k])
                nums1.pop()
                i+=1
        
