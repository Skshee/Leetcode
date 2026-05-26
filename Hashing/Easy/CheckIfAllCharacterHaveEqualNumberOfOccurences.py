class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = {}
       
        for char in s:
            if (char not in counts):
                counts[char]=1
            else:
                counts[char]+=1
        n = len(counts)
        
        # This is the part where I struggled. Didn't know how to iterate through the dictionary. What we're doing is instead storing all values(length of characters) in a list called frequencies and checking if the length of the set of frequencies is 1 i.e all characters have equal length
        frequencies = counts.values()
        if (len(set(frequencies))==1):
            return True
        else:
            return False

