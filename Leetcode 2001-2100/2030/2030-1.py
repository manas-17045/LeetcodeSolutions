# Leetcode 2030: Smallest K-Length Subsequence With Occurrences of a Letter
# https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/
# Solved on 30th of August, 2025
class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        """
        Finds the lexicographically smallest subsequence of length k from string s,
        such that it contains the specified 'letter' at least 'repetition' times.

        Args:
            s (str): The input string.
            k (int): The desired length of the subsequence.
            letter (str): The specific letter that must appear in the subsequence.
            repetition (int): The minimum number of times 'letter' must appear.

        Returns:
            str: The lexicographically smallest subsequence meeting the criteria.
        """
        sLength = len(s)
        lettersAvailable = s.count(letter)

        stack = []
        lettersInStack = 0

        for i, char in enumerate(s):
            while (stack and
                    stack[-1] > char and
                   (len(stack) - 1 + sLength - i) >= k):

                if stack[-1] == letter and lettersInStack - 1 + lettersAvailable < repetition:
                    break

                poppedChar = stack.pop()
                if poppedChar == letter:
                    lettersInStack -= 1

            if len(stack) < k:
                if char == letter:
                    stack.append(char)
                    lettersInStack += 1
                elif (k - len(stack)) > (repetition - lettersInStack):
                    stack.append(char)

            if char == letter:
                lettersAvailable -= 1

        return "".join(stack)