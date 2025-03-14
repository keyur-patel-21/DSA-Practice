class MyHashSet(object):

    def __init__(self):
        self.primaryBuckets = 1000
        self.secondaryBuckets = 1000
        self.storage = [None] * self.primaryBuckets

    def getPrimaryHash(self, key):
        return key % self.primaryBuckets

    def getSecondaryHash(self, key):
        return key // self.secondaryBuckets

    def add(self, key):
        primaryHash = self.getPrimaryHash(key)
        if self.storage[primaryHash] == None:
            if primaryHash == 0:
                self.storage[primaryHash] = [None] * (self.secondaryBuckets + 1)
            else:
                self.storage[primaryHash] = [None] * (self.secondaryBuckets)
        secondaryHash = self.getSecondaryHash(key)
        self.storage[primaryHash][secondaryHash] = True
        

    def remove(self, key):
        primaryHash = self.getPrimaryHash(key)
        if self.storage[primaryHash] == None:
            return
        secondaryHash = self.getSecondaryHash(key)
        if self.storage[primaryHash][secondaryHash] == None:
            return
        self.storage[primaryHash][secondaryHash] = False
        

    def contains(self, key):
        primaryHash = self.getPrimaryHash(key)

        if self.storage[primaryHash] == None:
            return False

        secondaryHash = self.getSecondaryHash(key)
        return self.storage[primaryHash][secondaryHash] == True
        
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)