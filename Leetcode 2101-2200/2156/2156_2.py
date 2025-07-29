# Leetcode 2156: Find Substring With Given Hash Value
# https://leetcode.com/problems/find-substring-with-given-hash-value/
# Solved on 29th of July, 2025
class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        """
        Finds the first substring of length k whose hash value matches the given hashValue.

        Args:
            s (str): The input string.
            power (int): The base for the polynomial rolling hash.
            modulo (int): The modulo for the hash calculation.
            k (int): The desired length of the substring.
            hashValue (int): The target hash value to match.
        Returns:
            str: The first substring of length k that matches the hashValue.
        """
        n = len(s)
        # Precompute power^k % modulo for use in removing the trailing character
        power_k = pow(power, k, modulo)

        def char_val(c: str) -> int:
            return ord(c) - ord('a') + 1

        rolling_hash = 0
        result_index = 0

        # Build rolling hash backwards over the string
        for i in range(n - 1, -1, -1):
            # Multiply current hash by p, then add val(s[i])
            rolling_hash = (rolling_hash * power + char_val(s[i])) % modulo

            # If we've grown beyond size k, subtract out the character at i + k
            if i + k < n:
                to_remove = char_val(s[i + k]) * power_k
                rolling_hash = (rolling_hash - to_remove) % modulo

            # Once we've processed at least k characters, check for match
            if (n - i) >= k and rolling_hash == hashValue:
                result_index = i

        return s[result_index:result_index + k]