# Leetcode 3271: Hash Divided String
# https://leetcode.com/problems/hash-divided-string/
# Solved on 23rd of June, 2025
class Solution:
    def stringHash(self, s: str, k: int) -> str:
        """
        Calculates a hash string based on the input string `s` and an integer `k`.

        The string `s` is divided into substrings of length `k`. For each substring,
        the hash values of its characters are summed. The hash value of a character
        is its 0-based index in the alphabet (e.g., 'a' is 0, 'b' is 1).
        The sum is then taken modulo 26 to get an index, which is converted back
        to a character. These resulting characters are concatenated to form the final hash string.

        Args:
            s (str): The input string.
            k (int): The length of each substring.
        Returns:
            str: The calculated hash string.
        """
        resultChars = []

        # Iterate through the string s with a step of k to get each substring of length k.
        for i in range(0, len(s), k):
            # Extract the current substring
            currentSubstring = s[i:(i + k)]

            currentSum = 0
            # Calculate the sum of hash values for characters in the current substring
            for charInSubstring in currentSubstring:
                # The hash value of a character is its 0-based index in the alphabet.
                hashValue = ord(charInSubstring) - ord('a')
                currentSum += hashValue

            # Find the remainder of the sum when divided by 26.
            hashedCharIndex = currentSum % 26

            # Convert the index back to a character.
            finalChar = chr(ord('a') + hashedCharIndex)

            # Append the resulting character to the list.
            resultChars.append(finalChar)

        # Join all the computed characters to form the final result string.
        return "".join(resultChars)