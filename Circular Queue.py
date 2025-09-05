
class Queue:
    def __init__(self):
        self.frontPointer = 0
        self.rearPointer = -1
        self.maxSize = 4
        self.queueLength = 0

        self.queueList = [0 for i in range(5)]
        
    def enqueue(self, data):
        if self.rearPointer < self.maxSize:
            self.rearPointer = self.rearPointer + 1
            self.queueList[self.rearPointer] = data
            self.queueLength = self.queueLength + 1
        else:
            if self.queueLength == self.maxSize + 1:  
                print("Queue full. Cannot enqueue")
        if self.queueLength == self.maxSize:
                self.rearPointer = -1
    
    def dequeue(self):
        if self.frontPointer < self.queueLength:
            self.queueList[self.frontPointer] = 0
            self.frontPointer = self.frontPointer +1
            self.queueLength = self.queueLength - 1
        else:
                print("Queue is empty. Cannot dequeue")

    def __str__(self):
        return f"{self.queueList}"


queueList = Queue()



queueList.enqueue(5)
queueList.enqueue(2)
print(queueList)
queueList.dequeue()
print(queueList)
queueList.enqueue(8)
queueList.enqueue(4)
queueList.enqueue(7)
queueList.enqueue(3)
print(queueList)
queueList.dequeue()
print(queueList)
queueList.dequeue()
print(queueList)
