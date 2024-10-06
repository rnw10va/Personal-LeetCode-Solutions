# Problem Name: 26. Remove Duplicates from Sorted Array
# Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i+1 < len(nums):
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])
            else:
                i+=1
        return len(nums)
        
