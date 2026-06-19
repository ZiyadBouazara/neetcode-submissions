class MinStack:

    def __init__(self):
        self.stack = []
        
        # data structure to keep track of previous minimums
        # -> getMin() will return the most current minimum
        # append(), appendleft(), pop(), and popleft() 
        self.minimums = deque()

# stack = [ 1, 2,  ]
# minimums = [ 1, 2 ]

    def push(self, val: int) -> None:
        # simply append to the stack
        self.stack.append(val)
        # either push to start of deque or end depending on if new minimum or not
        if not self.minimums: # if empty
            self.minimums.append(val)
        elif val <= self.minimums[0]:
            self.minimums.appendleft(val)
        else:
            self.minimums.append(val)

        

    def pop(self) -> None:
        # simply pop from stack
        num = self.stack.pop()
        # either pop from start of deque or end depending on which one matches
        if num == self.minimums[0]:
            self.minimums.popleft()
        else:
            self.minimums.pop()

    def top(self) -> int:
        # simply return top of stack
        return self.stack[-1]
        

    def getMin(self) -> int:
        # return first element of deque
        return self.minimums[0]