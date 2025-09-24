# Leetcode 1540: Can Convert String in K Moves
# https://leetcode.com/problems/can-convert-string-in-k-moves/
# Solved on 24th of September, 2025
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        """
        Determines if string s can be converted to string t within k operations.

        Args:
            s (str): The source string.
            t (str): The target string.
            k (int): The maximum number of operations allowed.

        Returns:
            (bool): True if s can be converted to t, False otherwise.
        """
        # If lengths differ, impossible
        if len(s) != len(t):
            return False

        # counts[shift] = how many letters need exactly `shift` forward moves
        counts = [0] * 26

        for cs, ct in zip(s, t):
            shift = (ord(ct) - ord(cs)) % 26
            if shift != 0:
                counts[shift] += 1

        for x in range(1, 26):
            m = counts[x]
            if m > 0:
                required = x + 26 * (m - 1)
                if required > k:
                    return False

        return True