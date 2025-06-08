'''
Link : https://leetcode.com/problems/longest-substring-without-repeating-characters/editorial/
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_length = 0
        left,right = 0,0
        
        while right < len(s):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length
    
    