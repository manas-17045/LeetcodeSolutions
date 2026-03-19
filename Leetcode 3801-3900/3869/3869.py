# Leetcode 3869: Count Fancy Numbers in a Range
# https://leetcode.com/problems/count-fancy-numbers-in-a-range/
# Solved on 19th of March, 2026
class Solution:
    def countFancy(self, l: int, r: int) -> int:
        """
        Counts the number of 'fancy' numbers in the range [l, r].
        A number is fancy if its digits are monotonic or if its digit sum is a 'good sum'.

        :param l: The lower bound of the range (inclusive).
        :param r: The upper bound of the range (inclusive).
        :return: The total count of fancy numbers within the specified range.
        """
        goodSums = set()
        for i in range(1, 140):
            strVal = str(i)
            if len(strVal) == 1:
                goodSums.add(i)
            elif all(strVal[j] > strVal[j - 1] for j in range(1, len(strVal))):
                goodSums.add(i)
            elif all(strVal[j] < strVal[j - 1] for j in range(1, len(strVal))):
                goodSums.add(i)

        def solve(n: int) -> int:

            if n == 0:
                return 0

            numStr = str(n)
            length = len(numStr)
            memo = {}

            def dp(idx, isBound, isZero, lastDigit, currentDir, digitSum):

                if idx == length:
                    if isZero:
                        return 0

                    if currentDir != 3 or digitSum in goodSums:
                        return 1

                    return 0

                state = (idx, isBound, isZero, lastDigit, currentDir, digitSum)
                if state in memo:
                    return memo[state]

                limit = int(numStr[idx]) if isBound else 9
                ans = 0
                for d in range(limit + 1):
                    nextBound = isBound and (d == limit)
                    if isZero:
                        if d == 0:
                            ans += dp(idx + 1, nextBound, True, -1, 0, 0)
                        else:
                            ans += dp(idx + 1, nextBound, False, d, 0, d)
                    else:
                        nextDir = currentDir
                        if currentDir == 0:
                            if d > lastDigit:
                                nextDir = 1
                            elif d < lastDigit:
                                nextDir = 2
                        elif currentDir == 1:
                            if d > lastDigit:
                                nextDir = 1
                            else:
                                nextDir = 3
                        elif currentDir == 2:
                            if d < lastDigit:
                                nextDir = 2
                            else:
                                nextDir = 3

                        ans += dp(idx + 1, nextBound, False, d, nextDir, digitSum + d)

                memo[state] = ans
                return ans

            return dp(0, True, True, -1, 0, 0)

        return solve(r) - solve(l - 1)