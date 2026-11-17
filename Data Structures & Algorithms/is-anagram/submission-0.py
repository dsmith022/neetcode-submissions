class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sGram = {}
        tGram = {}
        for char in s:
            if char in sGram:
                sGram[char] += 1
            else:
                sGram[char] = 1
        for char in t:
            if char in tGram:
                tGram[char] += 1
            else:
                tGram[char] = 1
        for char in sGram:
            if char not in tGram:
                return False
            if sGram[char] != tGram[char]:
                return False
        return True