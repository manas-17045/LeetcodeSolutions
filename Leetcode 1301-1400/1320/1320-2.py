# Leetcode 1320: Minimum Distance to Type a Word Using Two Fingers
# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/
# Solved on 30th of August, 2025
from functools import lru_cache


class Solution:
    def minimumDistance(self, word: str) -> int:
        """
        Calculates the minimum distance to type a given word on a 6-column keyboard layout
        using two fingers.

        Args:
            word (str): The word to be typed.
        Returns:
            int: The minimum total Manhattan distance traveled by the fingers.
        """
        if not word:
            return 0

        # helper function to map letter 0...25 to (r, c) on 6-columns layout
        def coord(idx: int):
            return divmod(idx, 6)  # (row, col)

        def manhattan(a: int, b: int) -> int:
            # a or b can be -1 meaning "finger not placed yet"
            if a == -1 or b == -1:
                return 0
            ar, ac = coord(a)
            br, bc = coord(b)
            return abs(ar - br) + abs(ac - bc)

        n = len(word)
        nums = [ord(ch) - ord('A') for ch in word]

        @lru_cache(None)
        def dp(idx: int, f1: int, f2: int) -> int:
            # idx: next character index to type
            # f1, f2: positions (0..25) of finger1 and finger2, or -1 for free
            if idx == n:
                return 0
            target = nums[idx]
            # Move finger1 to target
            cost1 = manhattan(f1, target) + dp(idx + 1, target, f2)
            # Move finger2 to target
            cost2 = manhattan(f2, target) + dp(idx + 1, f1, target)
            return min(cost1, cost2)

        return dp(0, -1, -1)