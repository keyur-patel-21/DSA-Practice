class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap(object):
    def __init__(self):
        self.storage = [Node(None, None) for _ in range(10**3)]

    def put(self, key, value):
        index = key % len(self.storage)
        curr = self.storage[index]

        # if curr is there or not?
        while curr.next:
            if curr.next.key == key:
                curr.next.value = value
                return
            curr = curr.next
        curr.next = Node(key, value)

    def get(self, key):
        index = key % len(self.storage)
        curr = self.storage[index]

        while curr.next:
            if curr.next.key == key:
                return curr.next.value
            curr = curr.next
        return -1

    def remove(self, key):
        index = key % len(self.storage)
        curr = self.storage[index]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
            

                

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)