# Leetcode 2375: Construct Smallest Number From DI String
# https://leetcode.com/problems/construct-smallest-number-from-di-string/



class Solution:
    def smallestNumber(self, pattern: str) -> str:
        """
        Solution: The key idea is to use a stack to keep track of the numbers that are decreasing. When we encounter
        an 'I', it means the sequence is increasing, so we pop all the numbers from the stack and append them to the
        result. When we encounter a 'D', it means the sequence is decreasing, so we push the current number onto the
        stack. We also need to push the last number onto the stack when we reach the end of the pattern. The stack is
        used to reverse the order of the decreasing sequence.
        """
        result = []
        stack = []
        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))
            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    result.append(stack.pop())
        return ''.join(result)