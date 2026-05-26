'''
Link : https://leetcode.com/problems/minimum-window-substring/description/
Time Complexity : O(n)
Topic : Hashing, Sliding Window
LeetCode Problem : 76. Minimum Window Substring
Difficulty : Hard
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        required = len(need)
        window = {}
        formed = 0
        left = 0
        minlen = float('inf')
        minWindow = (0,0)

        for right in range(len(s)):
            char = s[right]
            window[char] = 1 + window.get(char,0)

            if char in need and need[char] == window[char]:
                formed += 1

            while formed == required:
                size = right - left + 1
                if size < minlen:
                    minlen = size
                    minWindow = (left, right)

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        if minlen == float("inf"):
            return ""
        return s[minWindow[0]:minWindow[1] + 1] 

            
       

        