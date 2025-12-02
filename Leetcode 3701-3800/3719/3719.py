# Leetcode 3719: Longest Balanced Subarray I
# https://leetcode.com/problems/longest-balanced-subarray-i/
# Solved on 2nd of November, 2025
class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        """
        Finds the length of the longest balanced subarray.
        A subarray is balanced if the number of distinct even elements
        is equal to the number of distinct odd elements.

        Args:
            nums: A list of integers.
        Returns:
            The length of the longest balanced subarray.
        """
        arrayLength = len(nums)
        maxLength = 0
        for i in range(arrayLength):
            if arrayLength - i <= maxLength:
                break

            distinctEvens = set()
            distinctOdds = set()
            for j in range(i, arrayLength):
                currentNumber = nums[j]

                if currentNumber % 2 == 0:
                    distinctEvens.add(currentNumber)
                else:
                    distinctOdds.add(currentNumber)

                if len(distinctEvens) == len(distinctOdds):
                    currentLength = j - i + 1
                    if currentLength > maxLength:
                        maxLength = currentLength

        return maxLength