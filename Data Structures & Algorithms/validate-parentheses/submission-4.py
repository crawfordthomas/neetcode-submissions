class Solution:
    def isValid(self, s: str) -> bool:
        sets = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for char in s:
            if char in sets:
                stack.append(char)
            elif not stack or sets[stack.pop()] != char:
                return False
        
        if stack:
            return False
        
        return True