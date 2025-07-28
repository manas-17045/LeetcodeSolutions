# Leetcode 1316: Distinct Echo Substrings
# https://leetcode.com/problems/distinct-echo-substrings/
# Solved on 29th of July, 2025
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        """
        Calculates the number of distinct "echo" substrings in a given string.
        An echo substring is a string that can be formed by concatenating two identical halves (e.g., "abcabc").
        :param text: The input string.
        :return: The count of distinct echo substrings.
        """
        n = len(text)
        # Base and mods for double hashing
        base = 91138233
        mod1, mod2 = 10**9 + 7, 10**9 + 9

        # Precompute prefix hashes and powers
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)
        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)
        for i, ch in enumerate(text):
            code = ord(ch) - ord('a') + 1
            h1[i + 1] = (h1[i] * base + code) % mod1
            h2[i + 1] = (h2[i] * base + code) % mod2
            p1[i + 1] = (p1[i] * base) % mod1
            p2[i + 1] = (p2[i] * base) % mod2

        def get_hash(l: int, r: int):
            x1 = h1[r] - h1[l] * p1[r - l] % mod1
            if x1 < 0:
                x1 += mod1
            x2 = h2[r] - h2[l] * p2[r - l] % mod2
            if x2 < 0:
                x2 += mod2
            return (x1, x2)

        seen = set()
        # Try each half-length L
        for L in range(1, n // 2 + 1):
            # Slide window of size 2*L
            for i in range(n - 2 * L + 1):
                # Compare hash of [i:i+L) vs [i+L:i+2L)
                if get_hash(i, i + L) == get_hash(i + L, i + 2 * L):
                    # Record full substring hash to dedupe
                    seen.add(get_hash(i, i + 2 * L))

        return len(seen)