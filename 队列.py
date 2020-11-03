

class Wueue:
    def __init__(self, size=100):
        self.wueue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0  #队尾指针
        self.front = 0  #队首指针
    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear+1) % self.size
            self.wueue[self.rear] = element
        else:
            raise IndexError('队列为满')
    def pop(self):
        if not self.is_empty():
            self.front = (self.front+1) % self.size
            return self.wueue[self.front]
        else:
            raise IndexError('队列为空')
    def is_empty(self):   #判断队空
        return self.rear == self.front
    def is_filled(self):
        return (self.rear+1) % self.size == self.front



w = Wueue(5)
for i in range(4):
    w.push(i)
print(w.pop())
w.push(100)
print(w)