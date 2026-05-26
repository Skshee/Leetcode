# Method 1 : Can follow this method as well beats 98% of answers in terms of time complexity

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        chars = []
        print(s)
        for char in s:
            if(ord(char)>=97 and ord(char)<=122 or ord(char)>=48 and ord(char)<=57):
                chars.append(char)
        n = len(chars)
        string = "".join(chars)

        if(string == string[::-1]):
            return True
        else:
            return False


# Method 2 : Using isalnum() method (if allowed in interview)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s += c
        new_s = new_s.lower()
        return new_s == new_s[::-1]

