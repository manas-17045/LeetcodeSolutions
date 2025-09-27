# Leetcode 3340: Check Balanced String
# https://leetcode.com/problems/check-balanced-string/
# Solved on 26th of September, 2025
class Solution:
    def isBalanced(self, num: str) -> bool:
        """
        Checks if a given string of digits is balanced. A string is balanced if the sum of digits at even indices
        equals the sum of digits at odd indices.
        :param num: A string representing a number.
        :return: True if the string is balanced, False otherwise.
        """
        evenSum = 0
        oddSum = 0
        for i in range(len(num)):
            if i % 2 == 0:
                evenSum += int(num[i])
            else:
                oddSum += int(num[i])

        return evenSum == oddSum