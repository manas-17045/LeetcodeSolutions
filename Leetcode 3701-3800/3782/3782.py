# Leetcode 3782: Last Remaining Integer After Alternating Deletion Operations
# https://leetcode.com/problems/last-remaining-integer-after-alternating-deletion-operations/
# Solved on 24th of December, 2025
class Solution:
    def lastInteger(self, n: int) -> int:
        """
        This function finds the last remaining integer after alternating deletion operations.
        :param n: The initial number of integers from 1 to n.
        :return: The last remaining integer.
        """
        head = 1
        step = 1
        isLeft = True
        while n > 1:
            if not isLeft and n % 2 == 0:
                head += step

            step *= 2
            n = (n + 1) // 2
            isLeft = not isLeft

        return head