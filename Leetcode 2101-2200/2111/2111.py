# Leetcode 2111: Minimum Operations to Make the Array K-Increasing
# https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/
# Solved on 10th of December, 2025
import bisect


class Solution:
    def kIncreasing(self, arr: list[int], k: int) -> int:
        """
        Calculates the minimum operations to make the array k-increasing.

        Args:
            arr (list[int]): The input array.
            k (int): The k-increasing factor.

        Returns:
            int: The minimum number of operations required.
        """

        n = len(arr)
        minOperations = 0

        for i in range(k):
            tails = []
            subSequenceLength = 0

            for j in range(i, n, k):
                subSequenceLength += 1
                num = arr[j]

                if not tails or num >= tails[-1]:
                    tails.append(num)
                else:
                    idx = bisect.bisect_right(tails, num)
                    tails[idx] = num

            minOperations += subSequenceLength - len(tails)

        return minOperations