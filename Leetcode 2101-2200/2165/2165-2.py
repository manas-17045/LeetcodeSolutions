# Leetcode 2165: Smallest Value of the Rearranged Number
# https://leetcode.com/problems/smallest-value-of-the-rearranged-number/
# Solved on 4th of September, 2025
class Solution:
    def smallestNumber(self, num: int) -> int:
        """
        Given an integer num, rearrange its digits to form the smallest possible number.
        :param num: The input integer.
        :return: The smallest number that can be formed by rearranging the digits of num.
        """
        if num == 0:
            return 0

        s = list(str(abs(num)))

        if num > 0:
            s.sort()
            # Ensure no leading zero
            if s[0] == '0':
                for i in range(1, len(s)):
                    if s[i] != '0':
                        s[0], s[i] = s[i], s[0]
                        break
            return int("".join(s))
        else:
            s.sort(reverse=True)
            return -int("".join(s))