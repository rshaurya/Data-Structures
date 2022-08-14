
class Queue:
    q = []

    def __init__(self, a):
        if not isinstance(a, list):
            print("Only lits allowed.")
        else:
            self.q = a

    def next(self):
        try:
            return self.q.pop(-1)
        except IndexError:
            print("Entered an empty list! Insert some values")

    def append(self, x):
        self.q.append(x)
        return self.q

t = Queue([1,2,3,4,5])
print(t.next())
print(t.append(6))

