class MinStack:

    def __init__(self):
        # self.currMin = float("inf")
        self.stack = []  # value , currMin

    def push(self, value: int) -> None:
        if self.stack:
            if value < self.stack[-1][1]:
                self.stack.append([value, value])
            else:
                self.stack.append(
                    [value, self.stack[-1][1]]
                )  # pichle vale ka min he currmiinhai
        else:
            self.stack.append([value, value])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
