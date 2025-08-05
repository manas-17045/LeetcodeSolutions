# Leetcode 2195: Append K Integers With Minimal Sum
# https://leetcode.com/problems/append-k-integers-with-minimal-sum/
# Solved on 5th of August, 2025
class Solution:
    def minimalKSum(self, nums: list[int], k: int) -> int:
        """
        Appends k integers with the minimal sum to the given list of numbers.

        Args:
            nums: A list of integers.
            k: The number of integers to append.
        Returns:
            The minimal sum of the initial numbers and the k appended integers.
        """
        uniqueNums = sorted(list(set(nums)))

        currentSum = k * (k + 1) // 2

        # This is the upper bound of the integers we've hypothetically summed up.
        upperBound = k

        for num in uniqueNums:
            if nums <= upperBound:
                # If num is in our initial set {1, ..., upperBound}, we csn't use it.
                # Remove it from the sum.
                currentSum -= num

                # To keep k items, we must take the next available integer.
                upperBound += 1
                currentSum += upperBound
            else:
                break

        return currentSum