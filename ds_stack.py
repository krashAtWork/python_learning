class Stack:
    def  __init__(self):
        self.stack = list()
    def push(self, ele):
        self.stack.append(ele)
    def show(self):
        print(self.stack)
    def pop(self):
        if(len(self.stack) > 0):
            return self.stack.pop()
        else:
            return None;
    def peek(self):          
        if(len(self.stack) > 0):
            return(self.stack[len(self.stack)-1])
    def __str__(self)
        print(self.stack)


print( "Hello World")

stack1 = Stack()
stack1.push(1)
stack1.push(2)

stack1.show()
#popped = stack1.pop()
#print(popped)
peeked = stack1.peek()
print(peeked)
