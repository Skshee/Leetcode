'''
Link : https://leetcode.com/problems/divide-chocolates/
Reference: https://www.youtube.com/watch?v=Ppy9lvyMnuc
Complexity: O(nlog(sum(sweetness)))
Similar logic to Split Array Largest Sum
'''

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def canDivide(mid):
            chunks = 0
            curSweet = 0
            for s in sweetness:
                curSweet += s
                if curSweet >= mid:
                    chunks += 1
                    curSweet = 0
            return chunks >= k + 1

        left, right = 1, sum(sweetness)

        while left <= right:
            mid = (left + right) // 2
            if canDivide(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right
