class Queue:
    def __init__(self):
        stack1 = []
        stack2 = []

    def add(self, n):
        if len(self.stack2) > 0:
            self.empty(self.stack2, self.stack1)
        self.stack1.append(n)

    def remove(self):
        if len(self.stack1) > 0:
            self.empty(self.stack1, self.stack2)
        return self.stack2.pop()

    def empty(self, source, target):
        while len(source) > 0:
            target.append(source.pop())




