# Leetcode 2606: Find the Substring With Maximum Cost
# https://leetcode.com/problems/find-the-substring-with-maximum-cost/
# Solved on 18th of September, 2025
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: list[int]) -> int:
        """
        Calculates the maximum cost of a substring in 's'.

        Args:
            s (str): The input string.
            chars (str): A string of characters whose values are explicitly defined.
            vals (list[int]): A list of integer values corresponding to the characters in 'chars'.

        Returns:
            int: The maximum cost of any substring in 's'.
        """
        # Build mapping for provided chars
        mapA = {ch: v for ch, v in zip(chars, vals)}

        max_sum = 0
        cur = 0
        for ch in s:
            # Get character value: mapped value if present, otherwise alphabetical position
            val = mapA.get(ch, ord(ch) - ord('a') + 1)
            cur += val
            # If current sum becomes negative, rest to 0 (empty substring).
            if cur < 0:
                cur = 0
            # Track maximum seen
            if cur > max_sum:
                max_sum = cur

        return max_sum