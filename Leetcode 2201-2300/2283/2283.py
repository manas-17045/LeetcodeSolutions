# Leetcode 2283: Check if Number Has Equal Digit Count and Digit Value
# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/
# Solved on 7th of March, 2026
class Solution:
    def digitCount(self, num: str) -> bool:
        """
        Checks if for every index i in the range 0 <= i < n,
        the digit i occurs num[i] times in num.

        :param num: A string of digits.
        :return: True if the condition is met, False otherwise.
        """

        digitFreq = [0] * 10
        for char in num:
            digitFreq[int(char)] += 1

        for i in range(len(num)):
            if digitFreq[i] != int(num[i]):
                return False

        return True