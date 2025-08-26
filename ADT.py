
class Stack:
    def __init__(self, max):
        self.max = max
        self.stack = []
        self.top = -1

    def push(self, new):
        if self.top != self.max-1:
            self.top += 1
            self.stack.append(new)
        else:
            print("stack is full")
    
    def pop(self):
        if self.top != -1:
            self.stack.pop(self.top)
            self.top -= 1
        else:
            print("array is empty")
    


    def __str__(self):
        return f"{self.stack}"

newstack = Stack(max = 10)



newstack.push(7)
print(newstack)   
newstack.pop()
print(newstack)
