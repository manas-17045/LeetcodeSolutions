# Leetcode 3340: Check Balanced String
# https://leetcode.com/problems/check-balanced-string/
# Solved on 26th of September, 2025
class Solution:
    def isBalanced(self, num: str) -> bool:
        """
        Checks if a given number string is balanced. A number is balanced if the sum of its digits at even indices
        equals the sum of its digits at odd indices.
        :param num: A string representing the number.
        :return: True if the number is balanced, False otherwise.
        """
        even_sum = 0
        odd_sum = 0
        for i, ch in enumerate(num):
            d = ord(ch) - 48
            if i % 2 == 0:
                even_sum += d
            else:
                odd_sum += d

        return even_sum == odd_sum