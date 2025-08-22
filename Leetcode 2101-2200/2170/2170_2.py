# Leetcode 2170: Minimum Operations to Make the Array Alternating
# https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/
# Solved on 22nd of August, 2025
from collections import Counter

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of operations to make all elements at even indices equal
        and all elements at odd indices equal, with the constraint that the final even and odd
        elements must be different.
        :param nums: A list of integers.
        :return: The minimum number of operations.
        """
        n = len(nums)
        if n <= 1:
            return 0

        even = Counter()
        odd = Counter()
        for i, v in enumerate(nums):
            if i % 2 == 0:
                even[v] += 1
            else:
                odd[v] += 1

        even_top = even.most_common(2)
        odd_top = odd.most_common(2)

        ev1_val, ev1_cnt = (even_top[0][0], even_top[0][1]) if len(even_top) > 0 else (None, 0)
        ev2_val, ev2_cnt = (even_top[1][0], even_top[1][1]) if len(even_top) > 1 else (None, 0)
        od1_val, od1_cnt = (odd_top[0][0], odd_top[0][1]) if len(odd_top) > 0 else (None, 0)
        od2_val, od2_cnt = (odd_top[1][0], odd_top[1][1]) if len(odd_top) > 1 else (None, 0)

        if ev1_val != od1_val:
            return n - (ev1_cnt + od1_cnt)

        change_even_ops = n - (ev2_cnt + od1_cnt)
        change_odd_ops = n - (ev1_cnt + od2_cnt)

        return min(change_even_ops, change_odd_ops)