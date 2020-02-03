class Queue2Stacks():

    def __init__(self):

        self.instack = []
        self.outstack = []

    def __str__(self):
        return '{}'.format(self.instack)

    def enqueue(self, element):

        self.instack.append(element)

    def dequeue(self):

        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()


q = Queue2Stacks()
q.enqueue(2)
q.enqueue(12)
q.enqueue(312)
print(q)
print(q.dequeue())
print(q.instack)
q.enqueue(77)
print(q.instack)
print(q)