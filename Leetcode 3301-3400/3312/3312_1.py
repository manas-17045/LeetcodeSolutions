# Leetcode 3312: Sorted GCD Pair Queries
# https://leetcode.com/problems/sorted-gcd-pair-queries/
# Solved on 16th of June, 2025
import bisect


class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        """
        Given an array of integers nums and an array of integers queries, return an array
        answer where answer[i] is the i-th smallest value among all possible gcd(nums[j], nums[k])
        for 0 <= j < k < nums.length.

        The values gcd(nums[j], nums[k]) are sorted in non-decreasing order.

        Args:
            nums: A list of integers.
            queries: A list of integers representing the desired k-th smallest GCD values.

        Returns:
            A list of integers where answer[i] is the queries[i]-th smallest GCD value.
        """
        maxVal = max(nums)

        freq = [0] * (maxVal + 1)
        for x in nums:
            freq[x] += 1

        multiples = [0] * (maxVal + 1)
        for i in range(1, (maxVal + 1)):
            for j in range(i, (maxVal + 1), i):
                multiples[i] += freq[j]

        count = [0] * (maxVal + 1)
        for i in range(maxVal, 0, -1):
            numMultiples = multiples[i]
            pairs = numMultiples * (numMultiples - 1) // 2

            for j in range(i * 2, (maxVal + 1), i):
                pairs -= count[j]

            count[i] = pairs

        distinctGcdValues = []
        cumulativeCounts = []
        currentSum = 0
        for i in range(1, (maxVal + 1)):
            if count[i] > 0:
                distinctGcdValues.append(i)
                currentSum += count[i]
                cumulativeCounts.append(currentSum)

        answer = []
        for q in queries:
            idx = bisect.bisect_left(cumulativeCounts, (q + 1))
            answer.append(distinctGcdValues[idx])

        return answer