'''
Link: https://leetcode.com/problems/asteroid-collision/
Time Complexity : O(n)
Space Complexity : O(n)
'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:  # Collision occurs only when a is moving left and stack top is moving right
                # Loop keeps running until either a = 0 or a is bigger than all asteroids in stack
                diff = stack[-1] + a
                
                if diff < 0:
                    stack.pop()
                elif diff == 0:
                    a = 0
                    stack.pop()
                    break
                else:
                    a = 0
                    break
            if a:
                stack.append(a)
        
        return stack
                
