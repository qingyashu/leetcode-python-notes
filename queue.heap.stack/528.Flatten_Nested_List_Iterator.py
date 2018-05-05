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

## flattening in constructor
class NestedIterator1(object):

    def __init__(self, nestedList):
        self.arr = []
        self.flatten(nestedList)
        
    def flatten(self, nestedList):
        for item in reversed(nestedList):
            if item.isInteger():
                self.arr.append(item.getInteger())
            else:
                self.flatten(item.getList())

    def next(self):
        return self.arr.pop()

    def hasNext(self):
        return len(self.arr) > 0

## copy into a stack
class NestedIterator2(object):

    def __init__(self, nestedList):
        self.stack = [i for i in reversed(nestedList)]

    def next(self):
        if self.hasNext():
            return self.stack.pop().getInteger()

    def hasNext(self):
        while self.stack:
            if self.stack[-1].isInteger():
                return True
            l = self.stack.pop()
            for i in reversed(l.getList()):
                self.stack.append(i)
        return False
        
## use pointer and stack
class NestedIterator3(object):

    def __init__(self, nestedList):
        self.stack = [(0, nestedList)]

    def next(self):
        if self.hasNext():
            index, arr = self.stack[-1]
            self.stack[-1] = (index+1, arr)
            return arr[index].getInteger()

    def hasNext(self):
        while self.stack:
            index, arr = self.stack[-1]
            if index == len(arr):
                self.stack.pop()
                continue
            if arr[index].isInteger() is False:
                self.stack[-1] = (index+1, arr)
                self.stack.append((0, arr[index].getList()))
            else:
                return True
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())