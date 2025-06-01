import queue 

class MyStack:

    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def push(self, x: int) -> None:
        if self.q1.empty():
            self.q2.put(x)
        else:
            self.q1.put(x)

    def pop(self) -> int:
        if self.q1.empty() and self.q2.empty():
            return None

        if not self.q1.empty():
            while self.q1.qsize() > 1:
                self.q2.put(self.q1.get())
            return self.q1.get()
        else:
            while self.q2.qsize() > 1:
                self.q1.put(self.q2.get())
            return self.q2.get()

    def top(self) -> int:
        if self.q1.empty() and self.q2.empty():
            return None

        if not self.q1.empty():
            while self.q1.qsize() > 1:
                self.q2.put(self.q1.get())
            top_value = self.q1.get()
            self.q2.put(top_value)
            return top_value
        else:
            while self.q2.qsize() > 1:
                self.q1.put(self.q2.get())
            top_value = self.q2.get()
            self.q1.put(top_value)
            return top_value

    def empty(self) -> bool:
        return self.q1.empty() and self.q2.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()