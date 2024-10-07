# Problem Name: 55. Jump Game
# Problem Link: https://leetcode.com/problems/jump-game/description/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 0:
                for j in range(i-1,-1,-1):
                    if nums[j] > i - j or (nums[j] >= i - j and len(nums)-1==i):
                        break
                    elif j == 0:
                        return False
        return True
