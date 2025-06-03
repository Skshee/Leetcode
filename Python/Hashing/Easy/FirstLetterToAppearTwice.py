# Just create a set and add characters and if a character is already in the set, return it 
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for char in s:
            if(char in seen):
                return char
            seen.add(char)