class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # datastruct to hold each letter + count
        letters = {}
        # loop through s to assign then through t to check
        for char in s:
            letters[char] = letters.get(char, 0) + 1

        for char in t:
            if char not in letters or letters[char] == 0:
                return False
            letters[char] -= 1

        return True