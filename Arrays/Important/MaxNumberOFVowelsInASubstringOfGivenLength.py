'''
Link : https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?source=submission-noac
Time Complexity : O(n)
Topic : Arrays, Sliding Window
LeetCode Problem : 1456. Maximum Number of Vowels in a Substring of Given Length
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        maxCount = currCount = 0
        
        for i in range(len(s)):
            if s[i] in vowels:
                currCount += 1
            if i >= k:
                if s[i - k] in vowels:
                    currCount -= 1
            maxCount = max(maxCount, currCount)
        
        return maxCount
