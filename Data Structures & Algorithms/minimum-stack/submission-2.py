class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If min_stack is empty, the new val is the minimum.
        # Otherwise, compare val with the current minimum.
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            current_min = self.min_stack[-1]
            self.min_stack.append(min(val,current_min))
        
    def pop(self) -> None:
        del(self.stack[-1])
        if self.min_stack[-1] not in self.stack:
            self.min_stack = [x for x in self.min_stack if x!= self.min_stack[-1]]
        
    
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]

        
