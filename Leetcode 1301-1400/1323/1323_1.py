# Leetcode 1323: Maximum 69 Number
# https://leetcode.com/problems/maximum-69-number/
# Solved on 16th of August, 2025
class Solution:
    def maximum69Number(self, num: int) -> int:
        """
        Given a positive integer num consisting only of digits 6 and 9.
        Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

        :param num: An integer consisting only of digits 6 and 9.
        :return: The maximum number after changing at most one digit.
        """
        numString = str(num)
        charList = list(numString)

        for i in range(len(charList)):
            if charList[i] == '6':
                charList[i] = '9'
                break

        return int("".join(charList))