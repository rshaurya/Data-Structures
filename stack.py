
class Stack:
    stack = []

    def __init__(self, a):
        if not isinstance(a, list):
            print("Enter a list only!")
        else:
            self.stack = a
    
    def pop(self):
        try:
            return self.stack.pop(0)
        except IndexError:
            print("Entered an empty list! Insert some values.")
    
    def push(self, x):
        self.stack.insert(0, x)
        return self.stack

st = Stack([1,2,3,4,5])
print(st.pop())
print(st.push(15))
print(type(st))
