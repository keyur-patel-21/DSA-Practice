# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        self.stack = []
        self.nestedList = nestedList
        self.idx = 0
        self.dfs(self.nestedList)

    def dfs(self, nestedList):

        for ele in nestedList:
            if ele.isInteger():
                self.stack.append(ele.getInteger())
            else:
                self.dfs(ele.getList())
        

    def next(self):
        val = self.stack[self.idx]
        self.idx += 1
        return val 
        

    def hasNext(self):
        if self.idx == len(self.stack):
            return False
        return True
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())