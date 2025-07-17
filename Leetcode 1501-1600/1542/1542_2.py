# Leetcode 1542: Find Longest Awesome Substring
# https://leetcode.com/problems/find-longest-awesome-substring/
# Solved on 17th of July, 2025
class Solution:
    def longestAwesome(self, s: str) -> int:
        """
        Finds the length of the longest "awesome" substring.

        An "awesome" substring is one where at most one digit appears an odd number of times.

        The approach uses a bitmask to represent the parity of digit counts.
        Each bit in the mask corresponds to a digit (0-9). If the bit is 1,
        the digit appears an odd number of times; if 0, an even number of times.

        Args:
            s (str): The input string consisting of digits.

        Returns:
            int: The length of the longest awesome substring.
        """
        mask = 0
        n = len(s)

        first_occ = [n] * 1024
        first_occ[0] = -1

        ans = 1  # Any single digit is itself an awesome substring
        for i, ch in enumerate(s):
            d = ord(ch) - ord('0')
            # Flip the d-th bit
            mask ^= (1 << d)

            prev = first_occ[mask]
            if prev != n:
                ans = max(ans, i - prev)
            else:
                # Record the first time we see this mask
                first_occ[mask] = i

            # Also try flipping each bit once: allows exactly one odd count
            for b in range(10):
                alt = mask ^ (1 << b)
                prev = first_occ[alt]
                if prev != n:
                    ans = max(ans, i - prev)

        return ans