# Leetcode 1342: Number of Steps to Reduce a Number to Zero
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# Solved on 27th of February, 2026
class Solution:
    def numberOfSteps(self, num: int) -> int:
        """
        Calculates the number of steps to reduce a non-negative integer to zero.
        :param num: The integer to be reduced.
        :return: The total number of steps taken.
        """
        stepCount = 0

        while num > 0:
            if num & 1:
                num -= 1
            else:
                num >>= 1
            stepCount += 1

        return stepCount