def initialiseTree():
    ArrayNodes = [[0, 0, 0] for _ in range(100)] # [Value, LeftPointer, RightPointer]
    print("Tree initialised")
    RootPointer = -1
    FreePointer = 0
    return ArrayNodes, RootPointer, FreePointer

def addNode(NewValue):
    global ArrayNodes, RootPointer, FreePointer
    if FreePointer >= 100:
        print("Tree is full")
    else:
        ArrayNodes[FreePointer][0] = NewValue
        ArrayNodes[FreePointer][1] = -1
        ArrayNodes[FreePointer][2] = -1
        if RootPointer == -1:
            RootPointer = FreePointer
        else:
            CurrentPointer = RootPointer
            Placed = False
            while not Placed:
                if NewValue < ArrayNodes[CurrentPointer][0]:
                    if ArrayNodes[CurrentPointer][1] == -1:
                        ArrayNodes[CurrentPointer][1] = FreePointer
                        Placed = True
                    else:
                        CurrentPointer = ArrayNodes[CurrentPointer][1]
                else:
                    if ArrayNodes[CurrentPointer][2] == -1:
                        ArrayNodes[CurrentPointer][2] = FreePointer
                        Placed = True
                    else:
                        CurrentPointer = ArrayNodes[CurrentPointer][2]
        FreePointer += 1

def SearchNode(SearchValue):
    global ArrayNodes, RootPointer
    CurrentPointer = RootPointer
    while CurrentPointer != -1:
        if ArrayNodes[CurrentPointer][0] == SearchValue:
            return CurrentPointer
        elif SearchValue < ArrayNodes[CurrentPointer][0]:
            CurrentPointer = ArrayNodes[CurrentPointer][1]
        else:
            CurrentPointer = ArrayNodes[CurrentPointer][2]
    return -1

def InOrderTraversal(ArrayNodes, RootPointer):
    if RootPointer != -1:
        InOrderTraversal(ArrayNodes, ArrayNodes[RootPointer][0])
        print(ArrayNodes [RootPointer][1], end=" ")
        InOrderTraversal(ArrayNodes, ArrayNodes[RootPointer][2])

def PreOrderTraversal(ArrayNodes, RootPointer):
    if RootPointer != -1:
        print(ArrayNodes[RootPointer][1], end=" ")
        PreOrderTraversal(ArrayNodes, ArrayNodes[RootPointer][0])
        PreOrderTraversal(ArrayNodes, ArrayNodes[RootPointer][2])

def PostOrderTraversal(ArrayNodes, RootPointer):
    if RootPointer != -1:
        PostOrderTraversal(ArrayNodes, ArrayNodes[RootPointer][0])
        PostOrderTraversal(ArrayNodes, ArrayNodes[RootPointer][2])
        print(ArrayNodes[RootPointer][1], end=" ")

ArrayNodes, RootPointer, FreePointer = initialiseTree()
addNode(10)
addNode(5)
addNode(15)
addNode(3)
print(ArrayNodes)