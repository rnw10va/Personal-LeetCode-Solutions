# Problem Name: 167. Two Sum II - Input Array is Sorted
# Problem Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for numberIndex in range(len(numbers)):
            currentTarget = target - numbers[numberIndex]
            left = numberIndex + 1
            right = len(numbers) - 1
            mid = right - (right - left) // 2
            while left <= right:
                if numbers[mid] == currentTarget:
                    return [numberIndex+1, mid+1]
                elif numbers[mid] > currentTarget:
                    right = mid - 1
                    mid = right - (right - left) // 2
                else:
                    left = mid + 1
                    mid = right - (right - left) // 2
