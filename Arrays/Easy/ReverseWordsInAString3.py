class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        print(words)
        rev_words = []
        for word in words:
            rev_words.append(word[::-1])
        return " ".join(rev_words) # Converts the list to a string with each element separated by spaces
        