class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        checker = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c in checker:
                if stack and checker[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack 


        