class Node:
    def __init__(self, key, value):
        # use doubly link node
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table_size = 10003 #prime number
        self.array = [None] * self.table_size
    
    def hash(self, key):
        # use simple division hash
        return key % self.table_size

    def put(self, key: 'int', value: 'int') -> 'None':
        """
        value will always be non-negative.
        """
        index = self.hash(key)
        if self.array[index] == None:
            self.array[index] = Node(key, value)
        else:
            prev = None
            cur = self.array[index]
            while cur:
                if cur.key == key: #update node
                    cur.value = value
                    return
                prev = cur
                cur = cur.next
            cur = Node(key, value)
            cur.prev = prev
            prev.next = cur 
        

    def get(self, key: 'int') -> 'int':
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = self.hash(key)
        node = self.array[index]
        while node:
            if node.key == key:
                return node.value
            else:
                node = node.next
        return -1
        

    def remove(self, key: 'int') -> 'None':
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = self.hash(key)
        node = self.array[index]
        while node:
            if node.key == key:
                if node.prev is None:
                    self.array[index] = node.next
                else:
                    node.prev.next = node.next
                if node.next is None:
                    node.prev.next = None
                else:
                    node.next.prev = node.prev
            node = node.next
    


if __name__ == "__main__":
    hashmap = MyHashMap()
    hashmap.put(1, 1)
    hashmap.put(2, 2)
    print(hashmap.array[1])
    print(hashmap.get(1))
    hashmap.remove(2)
    print(hashmap.get(2))