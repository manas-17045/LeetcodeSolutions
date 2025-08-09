# Leetcode 2554: Maximum Number of Integers to Choose From a Range I
# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/
# Resolved on 9th of August, 2025
class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        """
        Given a list of banned integers, a maximum integer n, and a maximum sum maxSum,
        return the maximum number of integers that can be chosen from the range [1, n]
        such that their sum does not exceed maxSum and none of the chosen integers are in the banned list.

        Args:
            banned (list[int]): A list of banned integers.
            n (int): The maximum integer in the range [1, n].
            maxSum (int): The maximum allowed sum of the chosen integers.

        Returns:
            int: The maximum number of integers that can be chosen.
        """
        bannedSet = set(banned)
        count = 0
        currentSum = 0

        for num in range(1, (n + 1)):
            if num not in bannedSet:
                if currentSum + num <= maxSum:
                    currentSum += num
                    count += 1
                else:
                    break

        return count