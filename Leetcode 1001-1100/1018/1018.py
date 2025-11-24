# Leetcode 1018: Binary Prefix Divisible By 5
# https://leetcode.com/problems/binary-prefix-divisible-by-5/
# Solved on 24th of November, 2025
class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        """
        Given a binary array nums, return an array of booleans answer, where answer[i] is true if the binary number
        represented by nums[0] to nums[i] is divisible by 5.

        Args:
            nums (list[int]): A binary array (containing only 0s and 1s).
        Returns:
            list[bool]: An array of booleans indicating divisibility by 5 for each prefix.
        """
        currentNum = 0
        resultArr = []

        for digit in nums:
            currentNum = (currentNum * 2 + digit) % 5
            resultArr.append(currentNum == 0)

        return resultArr