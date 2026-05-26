'''
Link : https://leetcode.com/problems/implement-stack-using-queues/description/
Time Complexity : O(n) for pop and O(1) for push and top
Space Complexity : O(n)
'''
class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
        

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        while len(self.queue1) > 1:
            val = self.queue1.popleft()
            self.queue2.append(val)
        popped = self.queue1.popleft()

        for _ in range(len(self.queue2)):
            val = self.queue2.popleft()
            self.queue1.append(val)
        return popped

    def top(self) -> int:
        return self.queue1[-1]
        

    def empty(self) -> bool:
        if len(self.queue1) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()