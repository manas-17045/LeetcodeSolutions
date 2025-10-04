# Leetcode 3490: Count Beautiful Numbers
# https://leetcode.com/problems/count-beautiful-numbers/
# Solved on 4th of October, 2025
import collections


class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        """
        Counts the number of "beautiful numbers" within a given range [l, r].
        A number is beautiful if the product of its non-zero digits divides its sum of digits.

        :param l: The lower bound of the range (inclusive).
        :param r: The upper bound of the range (inclusive).
        :return: The count of beautiful numbers in the range [l, r].
        """
        P2_CAP = 6
        P3_CAP = 4
        P5_CAP = 2
        P7_CAP = 2

        memoizedFactors = {}

        def getPrimeFactors(n):
            if n in memoizedFactors:
                return memoizedFactors[n]

            factors = collections.defaultdict(int)
            if n == 0:
                memoizedFactors[n] = factors
                return factors

            temp = n
            while temp % 2 == 0:
                factors[2] += 1
                temp //= 2
            while temp % 3 == 0:
                factors[3] += 1
                temp //= 3
            while temp % 5 == 0:
                factors[5] += 1
                temp //= 5
            while temp % 7 == 0:
                factors[7] += 1
                temp //= 7
            if temp > 1:
                factors['other'] = 1

            memoizedFactors[n] = factors
            return factors

        digitFactors = {d: getPrimeFactors(d) for d in range(1, 10)}

        def solve(nStr):
            memo = {}
            sLen = len(nStr)

            def dp(index, isTight, isLeading, hasZero, currentSum, p2, p3, p5, p7):
                if index == sLen:
                    if isLeading:
                        return 0
                    if hasZero:
                        return 1
                    if currentSum == 0:
                        return 0

                    sumFactors = getPrimeFactors(currentSum)
                    if 'other' in sumFactors:
                        return 0

                    if p2 >= sumFactors[2] and p3 >= sumFactors[3] and p5 >= sumFactors[5] and p7 >= sumFactors[7]:
                        return 1
                    return 0

                state = (index, isTight, isLeading, hasZero, currentSum, p2, p3, p5, p7)
                if state in memo:
                    return memo[state]

                res = 0
                limit = int(nStr[index]) if isTight else 9

                for digit in range(limit + 1):
                    newTight = isTight and (digit == limit)

                    if isLeading and digit == 0:
                        res += dp(index + 1, newTight, True, False, 0, 0, 0, 0, 0)
                    else:
                        newHasZero = hasZero or (digit == 0)

                        if newHasZero:
                            res += dp(index + 1, newTight, False, True, 0, 0, 0, 0, 0)
                        else:
                            df = digitFactors[digit]
                            newSum = currentSum + digit
                            newP2 = min(P2_CAP, p2 + df[2])
                            newP3 = min(P3_CAP, p3 + df[3])
                            newP5 = min(P5_CAP, p5 + df[5])
                            newP7 = min(P7_CAP, p7 + df[7])
                            res += dp(index + 1, newTight, False, False, newSum, newP2, newP3, newP5, newP7)

                memo[state] = res
                return res

            return dp(0, True, True, False, 0, 0, 0, 0, 0)

        ansR = solve(str(r))
        ansLMinus1 = solve(str(l - 1))

        return ansR - ansLMinus1