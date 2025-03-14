"""
Approach:
1. **Hashing Mechanism**: This implementation of `MyHashSet` uses a **2D array (Bucket & Bucket-Items Approach)** 
   to efficiently store and retrieve elements.
2. **Hashing Strategy**: 
   - The `primaryBuckets` (1000) determine the main storage array.
   - The `secondaryBuckets` (1000) allow a secondary level of storage for better memory utilization.
   - `getPrimaryHash(key) = key % 1000` determines the index of the primary bucket.
   - `getSecondaryHash(key) = key // 1000` determines the index within the secondary bucket.
3. **Operations**:
   - `add(key)`: Checks if the primary bucket exists; if not, initializes it. Then, marks the corresponding secondary bucket as `True`.
   - `remove(key)`: Sets the value in the secondary bucket to `False`, indicating the key is removed.
   - `contains(key)`: Returns `True` if the key is present, otherwise `False`.

Time Complexity (TC):
- `add()`, `remove()`, and `contains()` operate in **O(1)** time since accessing and updating an array index is constant time.

Space Complexity (SC):
- In the worst case, when all `10^6` elements (max key constraint) are added, the space required is **O(10^6)**.
- However, due to lazy initialization, it is more efficient in terms of memory usage.
"""

class MyHashSet(object):

    def __init__(self):
        self.primarySize = 1000
        self.secondarySize = 1000
        self.primaryArray = [None] * self.primarySize

    def getPrimaryHash(self,key):
        return key % self.primarySize

    def getSecondaryHash(self,key):
        return key // self.secondarySize

    def add(self, key):
        primaryHash = self.getPrimaryHash(key)
        if self.primaryArray[primaryHash] == None:
            if primaryHash == 0:
                self.primaryArray[primaryHash] = [None] * (self.secondarySize+1)
            else:
                self.primaryArray[primaryHash] = [None] * (self.secondarySize)
        secondaryHash = self.getSecondaryHash(key)

        self.primaryArray[primaryHash][secondaryHash] = True
       
        

    def remove(self, key):
        primaryHash = self.getPrimaryHash(key)
        if self.primaryArray[primaryHash] == None:
            return
        secondaryHash = self.getSecondaryHash(key)

        if self.primaryArray[primaryHash][secondaryHash] is None:
            return
        self.primaryArray[primaryHash][secondaryHash] = None
        

    def contains(self, key):
        primaryHash = self.getPrimaryHash(key)
        if self.primaryArray[primaryHash] == None:
            return False
        secondaryHash = self.getSecondaryHash(key)

        return self.primaryArray[primaryHash][secondaryHash] == True
        
        
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)