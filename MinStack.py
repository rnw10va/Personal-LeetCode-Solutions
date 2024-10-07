# Problem Name: 155. Min Stack
# Problem Link: https://leetcode.com/problems/min-stack/description/

class MinStack:

    def __init__(self):
        self.stackOfMin=[]
        self.stack=[]

    def push(self, val: int) -> None:
        if len(self.stackOfMin)==0 or self.stackOfMin[-1]>val:
            self.stack.append(val)
            self.stackOfMin.append(val)
        else:
            self.stack.append(val)
            self.stackOfMin.append(self.stackOfMin[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.stackOfMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackOfMin[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
