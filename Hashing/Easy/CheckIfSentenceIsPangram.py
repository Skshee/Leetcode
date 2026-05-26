class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sett = set(sentence)
        if(len(sett)==26):
            return True
        else:
            return False