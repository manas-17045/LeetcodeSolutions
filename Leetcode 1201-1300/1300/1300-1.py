# Leetcode 1300: Sum of Mutated Array Closest to Target
# https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/
# Solved on 28th of August, 2025
import bisect


class Solution:
    def findBestValue(self, arr: list[int], target: int) -> int:
        """
        Finds the integer value such that if all elements in the array greater than this value
        are replaced by this value, the sum of the array is closest to the target.

        :param arr: A list of integers.
        :param target: The target integer sum.
        :return: The integer value that minimizes the absolute difference between the mutated array sum and the target.
        """
        arr.sort()
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        if target >= prefix[n]:
            return arr[-1]

        def getSum(value: int) -> int:
            idx = bisect.bisect_right(arr, value)
            currentSum = prefix[idx] + (n - idx) * value
            return currentSum

        left = 0
        right = arr[-1]

        while left < right:
            mid = (left + right) // 2
            if getSum(mid) < target:
                left = mid + 1
            else:
                right = mid

        sum1 = getSum(left - 1)
        diff1 = abs(sum1 - target)

        sum2 = getSum(left)
        diff2 = abs(sum2 - target)

        if diff1 <= diff2:
            return left - 1
        else:
            return left