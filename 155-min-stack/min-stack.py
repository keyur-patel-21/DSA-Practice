# Approach:
# The MinStack class uses two stacks to maintain the elements and track the minimum element efficiently.
# - stack1 stores all elements pushed to the stack.
# - stack2 stores the minimum element up to the current point.
# During the push operation, the value is appended to stack1, and stack2 stores the minimum of the current value and the top of stack2 (or the value itself if stack2 is empty).
# For the pop operation, both stacks are popped to remove the most recent element and its associated minimum.
# The top operation simply returns the last element in stack1.
# The getMin operation returns the top element of stack2, which represents the minimum element in the stack.

# Time Complexity:
# - push(): O(1) - appending to both stacks is a constant time operation.
# - pop(): O(1) - popping from both stacks is a constant time operation.
# - top(): O(1) - accessing the top of stack1 is a constant time operation.
# - getMin(): O(1) - accessing the top of stack2 is a constant time operation.

# Space Complexity:
# - O(n) - Two stacks are used to store the elements and the minimum values, where n is the number of elements in the stack.

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