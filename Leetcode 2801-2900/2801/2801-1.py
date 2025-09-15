# Leetcode 2801: Count Stepping Numbers in Range
# https://leetcode.com/problems/count-stepping-numbers-in-range/
# Solved on 15th of September, 2025
class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        """
        Counts the number of stepping numbers in the range [low, high].

        Args:
            low (str): The lower bound of the range as a string.
            high (str): The upper bound of the range as a string.
        Returns:
            int: The count of stepping numbers in the given range, modulo 10^9 + 7.
        """
        MOD = 10**9 + 7

        def solve(s: str) -> int:
            n = len(s)
            memo = {}

            def dfs(index: int, prevDigit: int, isTight: bool, isLeadingZero: bool) -> int:
                if index == n:
                    return 1

                state = (index, prevDigit, isTight, isLeadingZero)
                if state in memo:
                    return memo[state]

                res = 0
                upperBound = int(s[index]) if isTight else 9

                for digit in range(upperBound + 1):
                    newIsTight = isTight and (digit == upperBound)

                    if isLeadingZero:
                        if digit == 0:
                            res = (res + dfs(index + 1, 10, newIsTight, True)) % MOD
                        else:
                            res = (res + dfs(index + 1, digit, newIsTight, False)) % MOD
                    else:
                        if abs(digit - prevDigit) == 1:
                            res = (res + dfs(index + 1, digit, newIsTight, False)) % MOD

                memo[state] = res
                return res

            return dfs(0, 10, True, True)

        def subtractOne(s: str) -> str:
            n = len(s)
            sList = list(s)
            i = n - 1
            while i >= 0:
                if sList[i] == '0':
                    sList[i] = '9'
                    i -= 1
                else:
                    sList[i] = str(int(sList[i]) - 1)
                    break

            if n > 1 and sList[0] == '0':
                return "".join(sList[1:])

            return "".join(sList)

        countHigh = solve(high)

        lowMinusOne = subtractOne(low)
        countLowMinusOne = solve(lowMinusOne)

        result = (countHigh - countLowMinusOne + MOD) % MOD

        return result