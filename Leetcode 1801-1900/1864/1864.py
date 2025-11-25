# Leetcode 1864: Minimum Number of Swaps to Make the Binary String Alternating
# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/
# Solved on 25th of November, 2025
class Solution:
    def minSwaps(self, s: str) -> int:
        """
        Calculates the minimum number of swaps required to make a binary string alternating.

        Args:
            s (str): The input binary string.
        Returns:
            int: The minimum number of swaps, or -1 if it's not possible.
        """
        length = len(s)
        zeros = s.count('0')
        ones = length - zeros

        if abs(zeros - ones) > 1:
            return -1

        mismatches = 0
        for i, char in enumerate(s):
            expected = '0' if i % 2 == 0 else '1'
            if char != expected:
                mismatches += 1

        if zeros > ones:
            return mismatches // 2
        if ones > zeros:
            return (length - mismatches) // 2

        return min(mismatches, length - mismatches) // 2