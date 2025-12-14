# Leetcode 3448: Count Substrings Divisible By Last Digit
# https://leetcode.com/problems/count-substrings-divisible-by-last-digit/
# Solved on 14th of December, 2025
class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Counts the number of substrings in 's' that are divisible by their last digit.

        Args:
            s (str): The input string consisting of digits.
        Returns:
            int: The total count of such substrings.
        """
        totalCount = 0
        dp = [[0] * i for i in range(10)]

        for char in s:
            digit = int(char)
            for d in range(1, 10):
                nextDp = [0] * d
                currentDp = dp[d]

                for remainder, count in enumerate(currentDp):
                    if count > 0:
                        newRemainder = (remainder * 10 + digit) % d
                        nextDp[newRemainder] += count

                nextDp[digit % d] += 1

                dp[d] = nextDp

            if digit > 0:
                totalCount += dp[digit][0]

        return totalCount