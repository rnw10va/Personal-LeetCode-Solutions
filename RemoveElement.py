# Problem Name: 27. Remove Element
# Problem Link: https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = len(nums)
        i = 0
        while i < j:
            if nums[i] == val:
                nums.pop(i)
                nums.append('_')
                j-=1
            else:
                i+=1
        return i
