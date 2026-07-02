class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        MapS = {}
        MapT = {}
        for char in s:
            if char in MapS:
                MapS[char] += 1
            else:
                MapS[char] = 1
        for char in t:
            if char in MapT:
                MapT[char] += 1
            else:
                MapT[char] = 1

        if MapT == MapS:
            return True
        else:
            return False
        