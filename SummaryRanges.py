# Problem Name: 228. Summary Ranges
# Problem Link: https://leetcode.com/problems/summary-ranges/description/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        returnList = []
        startVal = None
        endVal = None
        for i in range(len(nums)):
            if startVal is None:
                startVal = nums[i]
            elif nums[i] == nums[i - 1] + 1:
                endVal = nums[i]
            elif endVal is None:
                returnList.append(str(startVal))
                startVal = nums[i]
                endVal = None
            else:
                returnList.append(str(startVal) + "->" + str(endVal))
                startVal = nums[i]
                endVal = None
        if startVal is not None and startVal == nums[-1]:
            returnList.append(str(nums[-1]))
        elif startVal is not None:
            returnList.append(str(startVal) + "->" + str(endVal))
        return returnList
