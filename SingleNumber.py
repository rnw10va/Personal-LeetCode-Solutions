# Problem Name: 136. Single Number
# Problem Link: https://leetcode.com/problems/single-number/description/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums2 = []
        for num in nums:
            if num in nums2:
                nums2.remove(num)
            else:
                nums2.append(num)
        return nums2[0]
