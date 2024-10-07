# Problem Name: 128. Longest Consecutive Sequence
# Problem Link: https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        dictionary = {}
        highestSequenceValue = 0
        for num in nums:
            biggerSequence=dictionary.get(num+1,0)
            smallerSequence=dictionary.get(num-1,0)
            currentSequenceMax=biggerSequence+smallerSequence+1
            dictionary[num]=currentSequenceMax
            dictionary[num+biggerSequence]=currentSequenceMax
            dictionary[num-smallerSequence]=currentSequenceMax
            highestSequenceValue=max(highestSequenceValue,currentSequenceMax)
        return highestSequenceValue
