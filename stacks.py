
class Stack:
    stack = []

    def __init__(self, a):
        self.stack = a
    
    def Pop(self):
        return self.stack.pop(0)
    
    def push(self, x):
        self.stack.insert(0, x)
        return self.stack

st = Stack([1,2,3,4,5])
print(st.Pop())
print(st.push(15))
print(type(st))
