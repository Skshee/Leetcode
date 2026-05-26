'''
Link : https://leetcode.com/problems/minimum-speed-to-arrive-on-time/
Complexity: O(n log(max(dist)))
'''

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        def totalTime(speed):
            hours = 0
            for i,distance in enumerate(dist):
                if i == n-1:
                    hours += distance/speed
                else:
                    hours += ceil(distance/speed)
            print(hours)
            return hours <= hour

        left, right = 1, 10**7
        answer = -1

        while left <= right:
            mid = (left + right) // 2
            if totalTime(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer