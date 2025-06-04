# Leetcode 3403: Find the Lexicographically Largest String From the Box I
# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/
# Solved on 4th of June, 2025

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        """
        Finds the lexicographically largest string that can be formed by taking a contiguous substring of length
        `len(word) - numFriends + 1` from the input word.

        Args:
            word: The input string.
            numFriends: The number of friends, which determines the length of the substring.

        Returns:
            The lexicographically largest substring of the specified length.
        """
        # If there is only one friend, the entire word is the answer.
        if numFriends == 1:
            return word

        # Get the length of the input word.
        n = len(word)
        # Initialize the maximum string found so far to an empty string.
        maxStr = ""

        # Iterate through all possible starting indices of substrings.
        for i in range(n):
            # Calculate the maximum possible length of a valid substring.
            # A valid substring must be formed by taking n - numFriends + 1 characters.
            maxLen = n - numFriends + 1
            # Calculate the ending index of the current substring, ensuring it doesn't exceed the word length.
            endIdx = min(i + maxLen, n)
            # Extract the current substring.
            subStr = word[i:endIdx]
            # Compare the current substring with the maximum string found so far.
            if subStr > maxStr:
                # If the current substring is lexicographically larger, update maxStr.
                maxStr = subStr

        # Return the lexicographically largest substring found.
        return maxStr