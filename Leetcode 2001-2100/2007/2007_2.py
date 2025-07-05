# Leetcode 2007: Find Original Array From Doubled Array
# https://leetcode.com/problems/find-original-array-from-doubled-array/
# Solved on 5th of July, 2025
from collections import Counter


class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        """
        Given a `changed` array, which is formed by appending twice the value of each element
        from an original array to itself, and then shuffling the resulting array.
        The task is to recover the original array. If no such original array exists,
        an empty array should be returned.

        The approach involves sorting the `changed` array and using a frequency counter.
        It iterates through the sorted `changed` array, attempting to find a corresponding
        double for each element.

        Args:
            changed (list[int]): The array formed by original + doubles, then shuffled.

        Returns:
            list[int]: The original array if it can be reconstructed, otherwise an empty list.
        """
        n = len(changed)
        # If odd total length, can't possibly be original + doubles
        if n % 2 == 1:
            return []

        changed.sort()
        freq = Counter(changed)
        original = []

        for x in changed:
            # If we've used up all of x already, skip it
            if freq[x] == 0:
                continue

            # Special case for zero: need pairs of zeros
            if x == 0:
                if freq[x] < 2:
                    return []
                # We can pull out freq[0]//2 zeros as original
                take = freq[x] // 2
                original.extend([0] * take)
                # Remove all zeros from freq
                freq[x] = 0
                continue

            # For non-zero x, we need its double available
            if freq[2 * x] < freq[x]:
                return []

            # Match every x with 2 * x
            count = freq[x]
            original.extend([x] * count)
            freq[2 * x] -= count
            freq[x] = 0

        # At this point, we've successfully paired every element
        return original