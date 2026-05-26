'''
Link : https://leetcode.com/problems/ransom-note/
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = defaultdict(int)
        magazine_dict = defaultdict(int)
        
        for char in ransomNote:
            ransom_dict[char] += 1
            
        for char in magazine:
            magazine_dict[char] += 1
            
        print(f"Magazine Dict:{magazine_dict}")
        print(f"Ransom Dict:{ransom_dict}")
        
        for char,freq in ransom_dict.items():
            if(char not in magazine_dict or magazine_dict[char] < freq):
                return False
        return True
                