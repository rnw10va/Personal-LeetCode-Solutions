# Problem Name: 74. Search a 2D Matrix
# Problem Link: https://leetcode.com/problems/search-a-2d-matrix/submissions/1219475659/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] < target:
                left = mid + 1
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                return True
        row = left - 1
        if row < 0:
            return False
        else:
            left = 0
            right = len(matrix[row]) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if matrix[row][mid] < target:
                    left = mid + 1
                elif matrix[row][mid] > target:
                    right = mid - 1
                else:
                    return True
            return False
