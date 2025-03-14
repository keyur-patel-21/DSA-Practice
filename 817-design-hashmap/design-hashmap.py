# Approach:
# - Implement a HashMap using separate chaining with linked lists.
# - The HashMap consists of an array of size 10^3, where each index stores a dummy head node.
# - Each bucket handles collisions using a linked list.
# - `put()`: If the key exists, update its value; otherwise, insert a new node at the end.
# - `get()`: Traverse the linked list in the corresponding bucket to find the key and return its value.
# - `remove()`: Traverse the linked list, find the key, and remove it by adjusting the next pointer.

# Time Complexity:
# - `put()`: O(N) in the worst case (when all elements hash to the same bucket), but O(1) on average.
# - `get()`: O(N) in the worst case, O(1) on average.
# - `remove()`: O(N) in the worst case, O(1) on average.
# - Here, N is the number of elements in a particular bucket.

# Space Complexity:
# - O(K), where K is the number of unique keys stored in the HashMap.
# - The storage array takes O(10^3) space, but actual space usage depends on inserted elements.


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap(object):

    def __init__(self):
        self.map = [Node(0,0) for i in range(10**4)]
        

    def put(self, key, value):
        index = key % len(self.map)
        cur = self.map[index]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = Node(key, value)
        

    def get(self, key):
        index = key % len(self.map)
        cur = self.map[index]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1
        

    def remove(self, key):
        index = key % len(self.map)
        cur = self.map[index]
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