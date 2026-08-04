class MyCircularQueue:

    def __init__(self, k: int):
        self.array = [-1] * k
        self.head = 0
        self.tail = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if not self.isFull() and self.array[self.tail % self.capacity] == -1:
            self.array[self.tail%self.capacity] = value
            self.tail += 1
            return True
        
        return False



    def deQueue(self) -> bool:
        if self.head < self.tail and self.array[self.head % self.capacity] != -1:
            self.array[self.head % self.capacity] = -1
            self.head += 1
            return True
        
        return False

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[self.head%self.capacity]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[(self.tail -1) % self.capacity]
        

    def isEmpty(self) -> bool:
        return self.head == self.tail
        

    def isFull(self) -> bool:
        return (self.tail - self.head) == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()