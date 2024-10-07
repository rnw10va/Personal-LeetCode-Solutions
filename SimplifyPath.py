# Problem Name: 71. Simplify Path
# Problem Link: https://leetcode.com/problems/simplify-path/description/

class Solution:
    def simplifyPath(self, path: str) -> str:
        #Use the stack for .. only
        path = path.split('/')
        canonicalPath = []
        for curPortion in path:
            if curPortion != '.' and curPortion != '' and curPortion != '..':
                canonicalPath.append(curPortion)
            elif canonicalPath and curPortion == '..': #If path contains something and there is a ..
                canonicalPath.pop()
        return '/' + '/'.join(canonicalPath)
