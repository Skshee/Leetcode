'''
Link : https://leetcode.com/problems/moving-average-from-data-stream/
Time Complexity : O(N)
Space Complexity : O(N)
'''

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.curr_size = 0

    def next(self, val: int) -> float:
        Sum = 0
        self.curr_size += 1
        self.queue.append(val)
        if self.curr_size > self.size:
            while self.curr_size > self.size:
                self.queue.popleft()
                self.curr_size -= 1

        for num in self.queue:
            Sum += num
        return Sum / self.curr_size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

# Faster Solution:

