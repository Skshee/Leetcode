# Link : https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Hint : Sliding Window
# Time Complexity : O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = right = 0
        res = 0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            res = max(res, right - left + 1)
        
        return res