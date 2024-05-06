class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given a string s containing just the characters:
            '(', ')', '{', '}', '[' and ']',
            determine if the input string is valid.

        An input string is valid if:

        1.Open brackets must be closed by the same type of brackets.
        2.Open brackets must be closed in the correct order.
        3.Every close bracket has a corresponding open bracket of the same type.
        
        Example 1:

        Input: s = "()"
        Output: true
        Example 2:

        Input: s = "()[]{}"
        Output: true
        Example 3:

        Input: s = "(]"
        Output: false
        """

        
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
        
        return not stack


solution = Solution()
print(solution.isValid("{}[{}]()"))
