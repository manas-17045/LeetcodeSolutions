# Leetcode 2264: Largest 3-Same-Digit Number in String
# https://leetcode.com/problems/largest-3-same-digit-number-in-string/
# Solved on 14th of August, 2025
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        """
        Finds the largest "good" integer (a 3-digit substring with all same digits) within a given string.

        :param num: The input string.
        :return: The largest good integer as a string, or an empty string if none exists.
        """
        maxGoodInteger = ""

        for i in range(len(num) - 2):
            substring = num[i:(i + 3)]
            if substring[0] == substring[1] and substring[1] == substring[2]:
                if substring > maxGoodInteger:
                    maxGoodInteger = substring

        return maxGoodInteger