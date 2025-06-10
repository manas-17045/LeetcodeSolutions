# Leetcode 2449: Minimum Number of Operations to make Arrays Similar
# https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/
# Solved on 2nd of November, 2024

class Solution:
    def makeSimilar(self, nums: list[int], target: list[int]) -> int:
        """
        Calculates the minimum number of operations to make two arrays similar.
        An operation consists of adding or subtracting 2 from an element.
        Two arrays are similar if they have the same elements, considering parity.

        Args:
            nums: The first array of integers.
            target: The second array of integers.
        """
        even_nums = []
        odd_nums = []
        even_target = []
        odd_target = []

        for num in nums:
            if num % 2 == 0:
                even_nums.append(num)
            else:
                odd_nums.append(num)

        for num in target:
            if num % 2 == 0:
                even_target.append(num)
            else:
                odd_target.append(num)

        even_nums.sort()
        odd_nums.sort()
        even_target.sort()
        odd_target.sort()

        total_diff = 0
        for i in range(len(even_nums)):
            total_diff += abs(even_nums[i] - even_target[i])
        for i in range(len(odd_nums)):
            total_diff += abs(odd_nums[i] - odd_target[i])

        return total_diff // 4