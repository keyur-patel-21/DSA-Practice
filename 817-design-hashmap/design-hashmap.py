class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap(object):

    def __init__(self):
        self.map = [Node(None, None) for _ in range(10**3)]
        

    def put(self, key, value):
        idx = key % len(self.map)
        curr = self.map[idx]

        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = Node(key, value)
        
    def get(self, key):
        idx = key % len(self.map)
        curr = self.map[idx]

        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return -1        

    def remove(self, key):
        idx = key % len(self.map)
        curr = self.map[idx]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)