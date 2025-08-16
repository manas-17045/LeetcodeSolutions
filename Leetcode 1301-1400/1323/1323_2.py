# Leetcode 1323: Maximum 69 Number
# https://leetcode.com/problems/maximum-69-number/
# Solved on 16th of August, 2025
class Solution:
    def maximum69Number(self, num: int) -> int:
        """
        Replaces the first occurrence of '6' with '9' in the given number to maximize it.
        :param num: An integer consisting only of digits 6 and 9.
        :return: The maximum possible number after at most one change.
        """
        pos = 0
        leftmost6_pos = -1
        tmp = num

        # Scan digits from least significant to most significant.
        while tmp > 0:
            if tmp % 10 == 6:
                leftmost6_pos = pos
            tmp = tmp // 10
            pos += 1

        # If no 6 found, return original number.
        if leftmost6_pos == -1:
            return num

        # Changing a 6 to 9 increases the number by 3 * 10^leftmost6_pos.
        return num + 3 * 10**leftmost6_pos