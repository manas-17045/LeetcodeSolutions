# Leetcode 1461: Check If a String Contains All Binary Codes of Size K
# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
# Solved on 18th of November, 2025
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """
        Checks if all possible binary codes of length k are present as substrings in s.

        Args:
            s (str): The input binary string.
            k (int): The length of the binary codes to check for.
        Returns:
            bool: True if all 2^k binary codes of length k are present in s, False otherwise.
        """
        totalNeeded = 1 << k

        if len(s) < k:
            return False

        foundCodes = set()
        bitMask = totalNeeded - 1
        currentValue = 0

        for i in range(k):
            currentValue = (currentValue << 1) | int(s[i])

        foundCodes.add(currentValue)

        for i in range(k, len(s)):
            currentValue = ((currentValue << 1) & bitMask) | int(s[i])
            foundCodes.add(currentValue)

        return len(foundCodes) == totalNeeded