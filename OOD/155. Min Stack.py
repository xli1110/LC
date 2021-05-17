class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.min_arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.min_arr:
            self.min_arr.append(val)
        else:
            self.min_arr.append(min(val, self.min_arr[-1]))

    def pop(self) -> None:
        if not self.arr:
            raise Exception("Empty Stack")
        self.arr.pop()
        self.min_arr.pop()

    def top(self) -> int:
        if not self.arr:
            raise Exception("Empty Stack")
        return self.arr[-1]

    def getMin(self) -> int:
        if not self.arr:
            raise Exception("Empty Stack")
        return self.min_arr[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
