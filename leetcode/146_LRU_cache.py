class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = []
        self.indexes = dict()

    def get(self, key: int) -> int:
        if self.indexes.get(key) is None:
            return -1
        
        index = self.indexes[key]
        value = self.items[index]
        self.put(key, value)
        return value


    def put(self, key: int, value: int) -> None:
        if len(self.items) == self.capacity:
            if self.indexes.get(key) is None:
                self.items.pop(0)
            else:
                index = self.indexes[key]
                self.items.pop(index)
            
        self.items.append(value)
        self.indexes[key] = len(self.items) - 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)       # returns 1
    cache.put(3, 3)    # evicts key 2
    cache.get(2)       # returns -1 (not found)
    cache.put(4, 4)    # evicts key 1
    cache.get(1)       # returns -1 (not found)
    cache.get(3)       # returns 3
    cache.get(4)       # returns 4