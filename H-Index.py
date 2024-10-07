# Problem Name: 274. H-Index
# Problem Link: https://leetcode.com/problems/h-index/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        hIndex = 0
        for citationIndex in range(len(citations)-1,-1,-1):
            hIndexCurrent = min(citationIndex+1,citations[citationIndex])
            if hIndexCurrent > hIndex:
                hIndex=hIndexCurrent
        return hIndex
            
