class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        pivot = 0
        for i in range(len(word)):
            if (word[i] == ch):
                pivot = i
                break
        if pivot == 0:
            return word 
        else:
            for i in range(pivot):
                return word[pivot::-1] + word[pivot+1::1]