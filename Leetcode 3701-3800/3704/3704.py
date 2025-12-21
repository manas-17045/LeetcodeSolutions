# Leetcode 3704: Count No-Zero Pairs That Sum to N
# https://leetcode.com/problems/count-no-zero-pairs-that-sum-to-n/
# Solved on 21st of December, 2025
class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        """
        Counts the number of pairs (a, b) such that a + b = n, and neither a nor b contains the digit 0.
        :param n: The target sum.
        :return: The number of no-zero pairs that sum to n.
        """
        s = str(n)[::-1]
        dp = [[[0] * 2 for _ in range(2)] for _ in range(2)]
        dp[0][0][0] = 1

        for i, char in enumerate(s):
            digit = int(char)
            newDp = [[[0] * 2 for _ in range(2)] for _ in range(2)]

            for carry in range(2):
                for aFinished in range(2):
                    for bFinished in range(2):
                        if dp[carry][aFinished][bFinished] == 0:
                            continue

                        for nextCarry in range(2):
                            targetSum = digit + 10 * nextCarry - carry

                            for nextAFinished in range(2):
                                for nextBFinished in range(2):
                                    if aFinished and not nextAFinished:
                                        continue
                                    if bFinished and not nextBFinished:
                                        continue

                                    if i == 0 and nextAFinished:
                                        continue
                                    if i == 0 and nextBFinished:
                                        continue

                                    ways = 0

                                    if nextAFinished and nextBFinished:
                                        if targetSum == 0:
                                            ways = 1
                                    elif nextAFinished and not nextBFinished:
                                        if 1 <= targetSum <= 9:
                                            ways = 1
                                    elif not nextAFinished and nextBFinished:
                                        if 1 <= targetSum <= 9:
                                            ways = 1
                                    else:
                                        if 2 <= targetSum <= 18:
                                            ways = 9 - abs(targetSum - 10)

                                    if ways > 0:
                                        newDp[nextCarry][nextAFinished][nextBFinished] += dp[carry][aFinished][
                                                                                              bFinished] * ways
            dp = newDp

        return sum(dp[0][af][bf] for af in range(2) for bf in range(2))