class MyQueue(object):

    def __init__(self):
        self.nStack = []
        self.qStack = [] 
        

    def push(self, x):
        self.nStack.append(x)
        

    def pop(self):
        if self.qStack:
            return self.qStack.pop()
        else:
            while self.nStack:
                self.qStack.append(self.nStack.pop())
            return self.qStack.pop()
        

    def peek(self):
        if self.qStack:
            return self.qStack[-1]
        else:
            while self.nStack:
                self.qStack.append(self.nStack.pop())
            return self.qStack[-1]
        

    def empty(self):
        if len(self.qStack) == 0 and len(self.nStack) == 0:
            return True
        else:
            return False 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()