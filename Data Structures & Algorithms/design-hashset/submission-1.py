class MyHashSet:

    def __init__(self):
        self.cap = 10007
        self.hmap = [[] for _ in range(self.cap)]
        
    def _hash(self, x) -> int:
        return x%self.cap

    def add(self, key: int) -> None:
        idx = self._hash(key)
        if key not in self.hmap[idx]:
            self.hmap[idx].append(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        if key in self.hmap[idx]:
            self.hmap[idx].remove(key)
        

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        if key in self.hmap[idx]:
            return True
        
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)