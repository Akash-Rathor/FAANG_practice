class Stack:
    
    def  __init__(self):
        self.stack = []
        
    
    def push(self,data):
        self.stack.append(data)
        
    def pop(self):
        return self.stack.pop()


def reverse(S):
    stack = Stack()
    for i in S:
        stack.push(i)
    
    data = []
    for i in S:
        data.append(stack.pop())
        
    
    return "".join(data)
    
S = 'geeks'
print(reverse(S))