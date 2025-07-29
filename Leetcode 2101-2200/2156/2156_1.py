# Leetcode 2156: Find Substring With Given Hash Value
# https://leetcode.com/problems/find-substring-with-given-hash-value/
# Solved on 29th of July, 2025
class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        """
        Finds the first substring of length k whose hash value matches the given hashValue.
        The hash value is calculated using the formula:
        hash(s, p, m) = (val(s[0]) * p^0 + val(s[1]) * p^1 + ... + val(s[k-1]) * p^(k-1)) % m
        where val(c) is the 1-indexed value of the character (e.g., 'a' is 1, 'b' is 2).

        Args:
            s (str): The input string.
            power (int): The base for the hash calculation.
            modulo (int): The modulo for the hash calculation.
            k (int): The desired length of the substring.
            hashValue (int): The target hash value to find.
        Returns:
            str: The first substring of length k that has the given hashValue, found by iterating from right to left.
        """

        n = len(s)
        resultIndex = -1

        # Calculate p^(k - 1) for the rolling hash update
        powerK_minus_1 = pow(power, k - 1, modulo)

        # Calculate the hash of the last substring: s[(n-k)...(n-1)]
        currentHash = 0
        p_i = 1
        for i in range(k):
            charValue = ord(s[n - k + i]) - ord('a') + 1
            currentHash = (currentHash + charValue * p_i) % modulo
            if i < (k - 1):
                p_i = (p_i * power) % modulo

        if currentHash == hashValue:
            resultIndex = n - k

        # Iterate from right to left to find the first valid substring
        for i in range(n - k - 1, -1, -1):
            valToRemove = ord(s[i + k]) - ord('a') + 1
            valToAdd = ord(s[i]) - ord('a') + 1

            # Remove the last character of the previous window
            termToRemove = (valToRemove * powerK_minus_1) % modulo
            currentHash = (currentHash - termToRemove + modulo) % modulo

            # Multiply by power to shift all powers up by one
            currentHash = (currentHash * power) % modulo

            # Add the new character at the beginning of the window
            currentHash = (currentHash + valToAdd) % modulo

            if currentHash == hashValue:
                resultIndex = i

        return s[resultIndex:resultIndex + k]