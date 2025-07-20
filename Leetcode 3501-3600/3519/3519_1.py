# Leetcode 3519: Count Numbers with Non-Decreasing Digits
# https://leetcode.com/problems/count-numbers-with-non-decreasing-digits
# Solved on 20th of July, 2025
class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        """
        Counts numbers with non-decreasing digits in a given base within a range.
        :param l: The lower bound of the range (as a string representing an integer in base 10).
        :param r: The upper bound of the range (as a string representing an integer in base 10).
        :param b: The base to consider for the non-decreasing digits.
        :return: The count of numbers with non-decreasing digits in base 'b' between 'l' and 'r' (inclusive), modulo 10^9 + 7.
        """
        mod = 10 ** 9 + 7
        maxLen = 350 + b

        C = [[0] * maxLen for _ in range(maxLen)]
        for i in range(maxLen):
            C[i][0] = 1
            for j in range(1, i + 1):
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % mod

        def toBase(nInt, base):
            if nInt == 0:
                return "0"

            digits = []
            while nInt > 0:
                digits.append(str(nInt % base))
                nInt //= base
            return "".join(reversed(digits))

        def count(s, base):
            if s == "0":
                return 0

            sNum = [int(d) for d in s]
            n = len(s)
            ans = 0

            for i in range(1, n):
                ans = (ans + C[base + i - 2][i]) % mod

            prevDigit = 1
            for i in range(n):
                digit = sNum[i]

                for d in range(prevDigit, digit):
                    rem = n - 1 - i
                    choices = base - d
                    ans = (ans + C[rem + choices - 1][rem]) % mod

                if digit < prevDigit:
                    return ans

                prevDigit = digit

            ans = (ans + 1) % mod
            return ans

        rInt = int(r)
        lInt = int(l)

        rBaseB = toBase(rInt, b)
        lMinusOneBaseB = toBase(lInt - 1, b)

        resR = count(rBaseB, b)
        resL = count(lMinusOneBaseB, b)

        result = (resR - resL + mod) % mod
        return result