# Leetcode 869: Reordered Power of 2
# https://leetcode.com/problems/reordered-power-of-2/
# Solved on 10th of August, 2025
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        """
        Checks if a given integer `n` can be reordered to form a power of 2.

        Args:
            n (int): The integer to check.
        Returns:
            bool: True if `n` can be reordered to form a power of 2, False otherwise.
        """
        target = self._digit_count(n)
        for i in range(31):
            if target == self._digit_count(1 << i):
                return True
        return False

    def _digit_count(self, x: int) -> tuple[int, ...]:
        counts = [0] * 10
        if x == 0:
            counts[0] = 1
        while x:
            counts[x % 10] += 1
            x //= 10
        return tuple(counts)