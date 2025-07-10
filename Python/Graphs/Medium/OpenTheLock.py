'''
Link : https://leetcode.com/problems/open-the-lock/
Reference : https://www.youtube.com/watch?v=Pzg3bCDY87w
Company : Meta
'''

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        def neighbours(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res

        visited = set(deadends)
        queue = deque()
        queue.append(['0000', 0]) # Lock and turns

        while queue:
            lock, turns = queue.popleft()

            if lock == target:
                return turns

            for nei in neighbours(lock):
                if nei not in visited:
                    queue.append([nei, turns + 1])
                    visited.add(nei) 
        return -1       