# Leetcode 1316: Distinct Echo Substrings
# https://leetcode.com/problems/distinct-echo-substrings/
# Solved on 29th of July, 2025
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        """
        Finds the number of distinct "echo" substrings in a given string.
        An echo substring is a string that can be formed by concatenating a substring with itself (e.g., "abcabc").

        Args:
            text (str): The input string.
        Returns:
            int: The number of distinct echo substrings.
        """
        textLength = len(text)
        distinctEchoes = set()

        primeBase = 31
        primeModulus = 1_000_000_007

        powersOfBase = [1] * (textLength + 1)
        for i in range(1, textLength + 1):
            powersOfBase[i] = (powersOfBase[i - 1] * primeBase) % primeModulus

        prefixHashes = [0] * (textLength + 1)
        for i in range(textLength):
            charValue = ord(text[i]) - ord('a') + 1
            prefixHashes[i + 1] = (prefixHashes[i] * primeBase + charValue) % primeModulus

        for halfLength in range(1, textLength // 2 + 1):
            fullLength = 2 * halfLength
            for startIndex in range(textLength - fullLength + 1):
                midIndex = startIndex + halfLength

                firstHalfHash = (prefixHashes[midIndex] - (prefixHashes[startIndex] * powersOfBase[
                    halfLength]) % primeModulus + primeModulus) % primeModulus

                secondHalfHash = (prefixHashes[startIndex + fullLength] - (prefixHashes[midIndex] * powersOfBase[
                    halfLength]) % primeModulus + primeModulus) % primeModulus

                if firstHalfHash == secondHalfHash:
                    if text[startIndex:midIndex] == text[midIndex:startIndex + fullLength]:
                        distinctEchoes.add(text[startIndex:startIndex + fullLength])

        return len(distinctEchoes)