class Queue:
    def __init__(self, max):
        self.max = max
        self.queue = [None for i in range(max)]
        self.length = -1
        self.rearPointer = -1
        self.frontPointer = 0

    def enqueue(self, new):
        if self.length != self.max:
            self.rearPointer += 1
            self.length += 1
            self.queue[self.rearPointer] = new
        else:
            print("error")

    
    def dequeue(self):
        if self.length != -1:
            self.queue[self.frontPointer] = None
            self.frontPointer += 1
            self.length -= 1
        else:
            print("error")



    def __str__(self):
        return f"{self.queue}"

newqueue = Queue(max = 10)


newqueue.enqueue(7)
print(newqueue)   
newqueue.enqueue(10)
newqueue.enqueue(32)
print(newqueue)
newqueue.dequeue()
print(newqueue)
