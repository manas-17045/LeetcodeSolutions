# Leetcode 3790: Smallest All-Ones Multiple
# https://leetcode.com/problems/smallest-all-ones-multiple/
# Solved on 8th of January, 2026
class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        """
        Finds the length of the smallest "all-ones" number that is a multiple of k.
        :param k: An integer.
        :return: The length of the smallest all-ones multiple, or -1 if no such multiple exists.
        """
        if k % 2 == 0 or k % 5 == 0:
            return -1

        number = 0
        for length in range(1, k + 1):
            number = (number * 10 + 1) % k
            if number == 0:
                return length

        return -1