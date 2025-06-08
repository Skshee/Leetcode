class Solution:
    def frequencySort(self, s: str) -> str:
        # We'll be using a Counter here to count the frequency of each character

        freq = Counter(s)

        # Sorting the characters in descending order
        sorted_chars = sorted(freq, key = freq.get, reverse= True) # Freq.get returns count of each character

        result = ''.join(char*freq[char] for char in sorted_chars)

        return result


