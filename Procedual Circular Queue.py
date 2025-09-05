queueList = [0 for i in range(5)]

rearPointer = -1
frontPointer = 0
maxSize = 4
length = 0

def enqueue(data):
    global rearPointer, frontPointer, maxSize, length
    if rearPointer < maxSize:
        rearPointer += 1
        queueList[rearPointer] = data
        length += 1
    else:
        if length == maxSize+1:
            print ("Queue is full cannot enqueue")
    
    if rearPointer == maxSize:
            rearPointer = -1

def dequeue():
    global rearPointer, frontPointer, maxSize, length
    if length != 0:
        queueList[frontPointer] = 0
        frontPointer += 1
        length -= 1
    else:
        print("Queue is empty, can't dequeue")


enqueue(5)
enqueue(2)
print(queueList)
dequeue()
print(queueList)
enqueue(8)
enqueue(4)
enqueue(7)
enqueue(3)
print(queueList)
dequeue()
print(queueList)

    

