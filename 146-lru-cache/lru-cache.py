class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.memory = {}

        self.head.next = self.tail
        self.tail.prev = self.head

    def removeNode(self, curr):
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        curr.next = None
        curr.prev = None

    def addToHead(self, curr):
        curr.next = self.head.next
        curr.prev = self.head
        self.head.next = curr
        curr.next.prev = curr

        

    def get(self, key):
        if key in self.memory:
            curr = self.memory[key]
            self.removeNode(curr)
            self.addToHead(curr)
            return curr.val
        else:
            return -1
        

    def put(self, key, value):
        if key in self.memory:
            curr = self.memory[key]
            curr.val = value
            self.removeNode(curr)
            self.addToHead(curr)
        else:
            if len(self.memory) == self.capacity:
                curr = self.tail.prev
                self.removeNode(curr)
                del self.memory[curr.key]

            curr = Node(key, value)
            self.addToHead(curr)
            self.memory[key] = curr
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)