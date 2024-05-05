class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize stack with -1 as the base index
        max_length = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)  # Push index of '(' to stack
            else:  # s[i] == ')'
                stack.pop()  # Pop the top element from stack
                if not stack:  # If stack becomes empty
                    stack.append(i)  # Push current index as new base
                else:
                    max_length = max(max_length, i - stack[-1])  # Update max_length
        
        return max_length
