'''
Link : https://leetcode.com/problems/jump-game-iii/
'''

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        n = len(arr)

        def isValid(num):
            return 0<=num<n

        queue = deque()
        queue.append(start)
        visit = set()
        visit.add(start)

        while queue:
            index = queue.popleft()

            if arr[index] == 0:
                return True

            if isValid(index + arr[index]) and (index + arr[index]) not in visit:
                queue.append(index + arr[index])
                visit.add(index + arr[index])

            if isValid(index - arr[index]) and (index - arr[index]) not in visit:
                queue.append(index - arr[index])
                visit.add(index + arr[index])
        return False

        