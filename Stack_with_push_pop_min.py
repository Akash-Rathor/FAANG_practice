class Stack:

    '''
    All methods with O(1) complexity to
    push : To Insert data in stack
    Pop : To remove data from stack
    min : To get minimum element from the stack
    '''
    minimum_stack = []

    def __init__(self,stack=[]):
        self.stack = stack
        
    def push(self,data):
        self.stack.append(data)
        if self.minimum_stack:
            if self.minimum_stack[-1]>data:
                self.minimum_stack.append(data)
        else:
            self.minimum_stack.append(data)
        return self.stack

    def pop(self):
        k = self.stack.pop()
        if self.minimum_stack[-1]==k:
            self.minimum_stack.pop()
        return self.stack

    @property
    def min(self):
        if self.minimum_stack:
            min_val = self.minimum_stack[-1]
            return min_val
        else:
            return None

Stack().push(4)
Stack().push(5)
Stack().push(7)
Stack().push(6)
Stack().push(8)
Stack().push(3)
print(Stack().min)
Stack().pop()
print(Stack().min)
Stack().pop()
print(Stack().min)
Stack().pop()
print(Stack().min)
Stack().pop()
print(Stack().min)
Stack().pop()
print(Stack().min)
Stack().pop()
print(Stack().min)

# output
'''
3
4
4
4
4
4
None
'''