# Problem Name: 80 Remove Duplicates from Sorted Array II
# Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        elif len(nums) == 2:
            return 2
        else:
            k = 0
            i = 2
            while i < len(nums) - k:
                if nums[i] == nums[i - 1] and nums[i] == nums[i - 2]:
                    nums.pop(i)
                    nums.append('_')
                    k+=1
                else:
                    i+=1
        return i
