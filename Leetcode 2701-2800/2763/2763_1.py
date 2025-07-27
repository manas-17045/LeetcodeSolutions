# Leetcode 2763: Sum of Imbalance Numbers of All Subarrays
# https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/
# Solved on 27th of July, 2025
class Solution:
    def sumImbalanceNumbers(self, nums: list[int]) -> int:
        """
        Calculates the sum of imbalance numbers for all possible subarrays of the given array `nums`.

        An imbalance number for a subarray is defined as the number of adjacent pairs (x, y) in the sorted
        unique elements of the subarray such that |x - y| > 1.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            int: The total sum of imbalance numbers across all subarrays.
        """
        numCount = len(nums)
        totalImbalance = 0

        for i in range(numCount):
            seenNumbers = set()
            imbalance = 0
            for j in range(i, numCount):
                currentNum = nums[j]

                if currentNum in seenNumbers:
                    # If the number is a duplicate, the set of unique elements
                    # doesn't change, so the imbalance is the same.
                    totalImbalance += imbalance
                    continue

                if not seenNumbers:
                    # First element in the subarray. Imbalance is 0.
                    imbalance = 0
                elif len(seenNumbers) == 1:
                    # Second unique element. Imbalance is 1 if they aren't adjacent, else 0.
                    firstNum = next(iter(seenNumbers))
                    if abs(currentNum - firstNum) > 1:
                        imbalance = 1
                    else:
                        imbalance = 0
                else:
                    # Third or more unique element. The recurrence now applies.
                    hasLeftNeighbor = (currentNum - 1) in seenNumbers
                    hasRightNeighbor = (currentNum + 1) in seenNumbers

                    imbalance += 1
                    if hasLeftNeighbor:
                        imbalance -= 1
                    if hasRightNeighbor:
                        imbalance -= 1

                seenNumbers.add(currentNum)
                totalImbalance += imbalance

        return totalImbalance