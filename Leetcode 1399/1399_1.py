# Leetcode 1399: Count Largest Group
# https://leetcode.com/problems/count-largest-group/

from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:
        def get_digit_sum(num: int) -> int:
            digit_sum = 0

            while num > 0:
                digit_sum += num % 10
                num //= 10
            return digit_sum

        group_sizes = Counter()

        for i in range(1, n + 1):
            d_sum = get_digit_sum(i)
            group_sizes[d_sum] += 1

        max_size = 0

        if group_sizes:
            max_size = max(group_sizes.values())

        count_of_largest_groups = 0
        if max_size > 0:
            for size in group_sizes.values():
                if size == max_size:
                    count_of_largest_groups += 1

        return count_of_largest_groups