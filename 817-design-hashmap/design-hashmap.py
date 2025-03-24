class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap(object):

    def __init__(self):
        self.map = [Node(0,0) for i in range(10*3)]
        

    def put(self, key, value):
        idx = key % len(self.map)
        cur = self.map[idx]

        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = Node(key, value)

    def get(self, key):
        idx = key % len(self.map)
        cur = self.map[idx]

        while cur.next:
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next

        return -1
        

    def remove(self, key):
        idx = key % len(self.map)
        cur = self.map[idx]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)