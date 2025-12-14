# Leetcode 3260: Find the Largest Palindrome Divisible by K
# https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/
# Solved on 14th of December, 2025
class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        """
        Finds the largest palindrome of length `n` that is divisible by `k`.

        Args:
            n: The desired length of the palindrome.
            k: The divisor.

        Returns:
            A string representing the largest palindrome of length `n` divisible by `k`.
        """

        if k == 1 or k == 3 or k == 9:
            return '9' * n

        if k == 2:
            if n == 1:
                return '8'
            return '8' + '9' * (n - 2) + '8'

        if k == 4:
            if n <= 4:
                return '8' * n
            return '88' + '9' * (n - 4) + '88'

        if k == 5:
            if n == 1:
                return '5'
            return '5' + '9' * (n - 2) + '5'

        if k == 6:
            if n == 1:
                return '6'
            if n == 2:
                return '66'
            if n % 2 == 1:
                midLen = (n - 3) // 2
                return '8' + '9' * midLen + '8' + '9' * midLen + '8'
            else:
                midLen = (n - 4) // 2
                return '8' + '9' * midLen + '77' + '9' * midLen + '8'

        if k == 8:
            if n <= 6:
                return '8' * n
            return '888' + '9' * (n - 6) + '888'

        if k == 7:
            if n == 1:
                return '7'

            mod = (pow(10, n, 7) - 1) % 7
            mid = n // 2

            if n % 2 == 1:
                posVal = pow(10, mid, 7)
                for d in range(9, -1, -1):
                    if (mod + (d - 9) * posVal) % 7 == 0:
                        return '9' * mid + str(d) + '9' * mid
            else:
                posVal = (pow(10, mid, 7) + pow(10, mid - 1, 7)) % 7
                for d in range(9, -1, -1):
                    if (mod + (d - 9) * posVal) % 7 == 0:
                        left = '9' * (mid - 1)
                        return left + str(d) * 2 + left

        return ""