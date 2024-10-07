# Problem Name: 45. Jump Game II
# Problem Link: https://leetcode.com/problems/jump-game-ii/description/

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        jumpCount=1
        i=0
        currentMax=i+nums[i]
        while currentMax<len(nums)-1:
            jumpCount+=1
            newMax=i+1+nums[i+1]
            newi=i+1
            for j in range(i+2,currentMax+1):
                jMax=j+nums[j]
                if jMax>len(nums)-2:
                    return jumpCount
                elif newMax<jMax:
                    newMax=jMax
                    newi=j
            i=newi
            currentMax=newMax
        return jumpCount
