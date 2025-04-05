class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.memory = {}

    def removeNode(self, curr):
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        curr.next = None
        curr.prev = None

    def addToHead(self, curr):
        curr.next = self.head.next
        curr.prev = self.head
        curr.next.prev = curr
        self.head.next = curr

    def get(self, key):
        if key in self.memory:
            curr = self.memory[key]
            self.removeNode(curr)
            self.addToHead(curr)
            return curr.value
        return -1

    def put(self, key, value):
        if key in self.memory:
            curr = self.memory[key]
            curr.value = value
            self.removeNode(curr)
            self.addToHead(curr)
        else:
            if self.capacity == len(self.memory):
                node = self.tail.prev
                self.removeNode(node)
                del self.memory[node.key]
                
            curr = Node(key, value)
            self.addToHead(curr)
            self.memory[key] = curr
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)