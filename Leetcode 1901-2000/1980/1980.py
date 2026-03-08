# Leetcode 1980: Find Unique Binary String
# https://leetcode.com/problems/find-unique-binary-string/
# Solved on 8th of March, 2026
class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        """
        Finds a binary string of length n that does not appear in the given list of n binary strings.
        Uses Cantor's Diagonal Argument to ensure the generated string is unique.

        :param nums: A list of n binary strings, each of length n.
        :return: A binary string of length n that is not present in nums.
        """
        resultString = []

        for i in range(len(nums)):
            if nums[i][i] == '0':
                resultString.append('1')
            else:
                resultString.append('0')

        return "".join(resultString)