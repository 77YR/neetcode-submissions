class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        s1 = s
        s = ""
        for char in s1:
            if char.isalnum():
                s += char
        
        print(s)

        a = 0
        b = len(s)-1
    
        while (a < b):
            if (s[a] != s[b]):
                return False
            a += 1
            b -= 1
        return True
        