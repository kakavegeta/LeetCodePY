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
        # division hash
        return key % self.table_size

    def put(self, key: 'int', value: 'int') -> 'None':
        """
        value will always be non-negative.
        """
        index = self.hash(key)
        if self.array[index] == None:
            self.array[index] = Node(key, value)
        else:
            cur = self.array[index]
            prev = None
            while cur:
                if cur.key == key: #update node
                    cur.value = value
                    return
                prev = cur
                cur = cur.next
            prev.next = Node(key, value)
            prev.next.prev = prev

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
                if node.prev is None and node.next is None:
                    self.array[index] = None
                else:
                    if node.prev is None:
                        self.array[index] = node.next
                    else:
                        node.prev.next = node.next
                    if node.next is None:
                        node.prev.next = None 
                    else:
                        node.next.prev = node.prev

            node = node.next

class HashTable:
    # open addressing
    m, n = 10003, 10000
    def __init__(self):
        self.array = [None] * self.m
    
    def hash(self, key, i):
        return (key%self.m + i*(1 + key%self.n)) % self.m
    
    def put(self, key, value):
        for i in range(self.m):
            index = self.hash(key, i)
            if self.array[index] is None:
                self.array[index] = (key, value)
                return
            elif self.array[index][0] == key:
                self.array[index] = (key, value)
                return
        
    def get(self, key):
        for i in range(self.m):
            index = self.hash(key, i)
            if self.array[index] is None:
                return -1
            elif self.array[index][0] == key:
                return self.array[index][1]
        return -1
    
    def remove(self, key):
        for i in range(self.m):
            index = self.hash(key, i)
            if self.array[index] is None:
                return
            elif self.array[index][0] == key:
                self.array[index] = "Del"
                return 
    
        
            

    


if __name__ == "__main__":
    hashmap = MyHashMap()
    hashmap.put(1, 1)
    hashmap.put(2, 2)
    print(hashmap.array[1])
    print(hashmap.get(1))
    hashmap.remove(2)
    print(hashmap.get(2))