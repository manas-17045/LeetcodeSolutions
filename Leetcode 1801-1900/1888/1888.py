# Leetcode 1888: Minimum Number of Flips to Make the Binary String Alternating
# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/
# Solved on 7th of March, 2026
class Solution:
    def minFlips(self, s: str) -> int:
        """
        Calculates the minimum number of flips to make a binary string alternating,
        allowing for Type-1 operations (circular shifts).

        Args:
            s (str): A binary string consisting of '0's and '1's.

        Returns:
            int: The minimum number of flips required.
        """
        n = len(s)
        diff1 = 0
        diff2 = 0
        ans = float('inf')

        for i in range(2 * n):
            target1 = '0' if i % 2 == 0 else '1'
            target2 = '1' if i % 2 == 0 else '0'

            if s[i % n] != target1:
                diff1 += 1
            if s[i % n] != target2:
                diff2 += 1

            if i >= n:
                oldTarget1 = '0' if (i - n) % 2 == 0 else '1'
                oldTarget2 = '1' if (i - n) % 2 == 0 else '0'

                if s[(i - n) % n] != oldTarget1:
                    diff1 -= 1
                if s[(i - n) % n] != oldTarget2:
                    diff2 -= 1

            if i >= n - 1:
                if diff1 < ans:
                    ans = diff1
                if diff2 < ans:
                    ans = diff2

        return ans