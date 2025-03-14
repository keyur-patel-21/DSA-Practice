class MinStack(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, val):
        self.stack1.append(val)
        self.stack2.append(min(val, self.stack2[-1] if self.stack2 else val))
        

    def pop(self):
        self.stack1.pop()
        self.stack2.pop()
        

    def top(self):
        return self.stack1[-1]
        

    def getMin(self):
        return self.stack2[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()