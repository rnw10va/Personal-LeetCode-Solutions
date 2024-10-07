# Problem Name: 189. Rotate Array
# Problem Link: https://leetcode.com/problems/rotate-array/description/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        tempList = []
        if k > len(nums):
            k = k % len(nums)
        if k != 0:
            for i in range(len(nums)):
                if i < k:
                    tempList.append(nums[i-k])
                else:
                    var = nums[i-k]
                    nums[i-k] = tempList[j]
                    tempList[j] = var
                    j+=1
                    if j == k:
                        j=0
            for i in range(j,k):
                nums[i-k-j] = tempList[i]
            for i in range(j):
                nums[i-j] = tempList[i]
