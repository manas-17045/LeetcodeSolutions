# Leetcode 3827: Count Monobit Integers
# https://leetcode.com/problems/count-monobit-integers/
# Solved on 7th of February, 2026
class Solution:
    def countMonobit(self, n: int) -> int:
        """
        Counts the number of monobit integers (integers consisting only of 1s in binary) up to n.

        :param n: The upper limit integer.
        :return: The total count of monobit integers less than or equal to n.
        """
        totalCount = 1
        currentNum = 1

        while currentNum <= n:
            totalCount += 1
            currentNum = (currentNum << 1) | 1

        return totalCount