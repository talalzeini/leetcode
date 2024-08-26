class Solution:
    def isValid(self, s: str) -> bool:

        # Time Complexity: O(n)
        # Space Complexity: O(n)
        
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            print(c)
            if c in Map:
                if not stack or Map[c] != stack[len(stack) - 1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return not stack