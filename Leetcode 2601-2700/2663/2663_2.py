# Leetcode 2663: Lexicographically Smallest Beautiful String
# https://leetcode.com/problems/lexicographically-smallest-beautiful-string/
# Solved on 26th of June, 2025
class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        """
        Finds the lexicographically smallest "beautiful" string that is strictly greater than `s`.

        A string is beautiful if it has no palindromic substring of length 2 or 3.
        This means:
        - No two adjacent characters are the same (e.g., "aa" is not allowed).
        - No character is the same as the character two positions before it (e.g., "aba" is not allowed).
        The string must consist of the first `k` lowercase English letters.
        """
        n = len(s)
        # Convert characters to 0...(k - 1)
        a = [ord(c) - ord('a') for c in s]

        def validAt(pos: int, x: int) -> bool:
            # No palindrome of length2: neighbor must differ
            if pos > 0 and a[pos - 1] == x:
                return False
            # No palindrome of length 3: a[pos - 2] != x
            if pos > 1 and a[pos - 2] == x:
                return False
            return True

        # Try to bump position i
        for i in range(n - 1, -1, -1):
            # Remove old a[i] so validAt sees previous suffix as if it's unfilled
            old = a[i]
            # Try all larger letters
            for x in range(old + 1, k):
                if validAt(i, x):
                    a[i] = x
                    # Now, fill suffix (i + 1)...(n - 1) lexicographically minimally
                    ok = True
                    for j in range(i + 1, n):
                        placed = False
                        for y in range(k):
                            if validAt(j, y):
                                a[j] = y
                                placed = True
                                break
                        if not placed:
                            ok = False
                            break
                    if ok:
                        # Convert back and return
                        return "".join(chr(c + ord('a')) for c in a)
            # Restore and move left
            a[i] = old

        # No solution
        return ""