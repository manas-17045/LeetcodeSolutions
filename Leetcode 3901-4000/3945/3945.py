# Leetcode 3945: Digit Frequency Score
# https://leetcode.com/problems/digit-frequency-score/
# Solved on 12th of June, 2026
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        """
        Calculates the sum of the digits of a given integer.

        :param n: The input integer to process.
        :return: The total sum of all digits in n.
        """
        digitSum = 0
        while n > 0:
            digitSum += n % 10
            n //= 10

        return digitSum