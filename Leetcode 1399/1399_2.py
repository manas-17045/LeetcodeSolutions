# Leetcode 1399: Count Largest Group
# https://leetcode.com/problems/count-largest-group/

class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = {}

        for num in range(1, n + 1):
            digit_sum = self.sum_of_digits(num)

            if digit_sum in groups:
                groups[digit_sum] += 1
            else:
                groups[digit_sum] = 1

        max_size = max(groups.values()) if groups else 0

        count = sum(1 for size in groups.values() if size == max_size)

        return count

    def sum_of_digits(self, num: int) -> int:
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        return total