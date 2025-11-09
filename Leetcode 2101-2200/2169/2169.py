# Leetcode 2169: Count Operations to Obtain Zero
# https://leetcode.com/problems/count-operations-to-obtain-zero/
# Solved on 9th of November, 2025
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        """
        Counts the number of operations required to make either num1 or num2 zero.
        An operation consists of subtracting the smaller number from the larger number.

        :param num1: The first non-negative integer.
        :param num2: The second non-negative integer.
        :return: The total number of operations performed.
        """
        operationCount = 0
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                quotient = num1 // num2
                num1 = num1 * num2
                operationCount += quotient
            else:
                quotient = num2 // num1
                num2 = num2 * num1
                operationCount += quotient

        return operationCount