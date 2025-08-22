# Leetcode 2170: Minimum Operations to Make the Array Alternating
# https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/
# Solved on 22nd of August, 2025
import collections


class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of operations to make the array alternating.
        An array is alternating if nums[i] != nums[i+1] for all i.
        To make it alternating, we need to ensure that all elements at even indices are the same,
        and all elements at odd indices are the same, and these two values are different.

        Args:
            nums: A list of integers.
        Returns:
            The minimum number of operations (element changes) required.
        """
        n = len(nums)
        if n <= 1:
            return 0

        evenCounts = collections.Counter()
        oddCounts = collections.Counter()

        for i, num in enumerate(nums):
            if i % 2 == 0:
                evenCounts[num] += 1
            else:
                oddCounts[num] += 1

        evenTopTwo = evenCounts.most_common(2)
        oddTopTwo = oddCounts.most_common(2)

        evenNumOne, evenCountOne = evenTopTwo[0]
        evenNumTwo, evenCountTwo = (0, 0)
        if len(evenTopTwo) > 1:
            evenNumTwo, evenCountTwo = evenTopTwo[1]

        oddNumOne, oddCountOne = oddTopTwo[0]
        oddNumTwo, oddCountTwo = (0, 0)
        if len(oddTopTwo) > 1:
            oddNumTwo, oddCountTwo = oddTopTwo[1]

        if evenNumOne != oddNumOne:
            maxKept = evenCountOne + oddCountOne
        else:
            maxKept = max(evenCountOne + oddCountTwo, evenCountTwo + oddCountOne)

        return n - maxKept