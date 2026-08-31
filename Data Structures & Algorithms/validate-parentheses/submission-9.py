class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return False

        stack = []
        opens = "[{("
        close ={ "]" : "[",
                 "}" : "{",
                 ")" : "("}



        for char in s:
            if (char in opens):
                stack.append(char)
                print("append " + char + "\n")
            else:
                if not stack:
                    return False
                ch = stack.pop()
                if (close.get(char) is not ch):
                    return False
        if stack:
            return False
        return True

        