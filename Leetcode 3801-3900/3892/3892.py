# Leetcode 3892: Minimum Operations to Achieve At Least K Peaks
# https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/
# Solved on 12th of April, 2026
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum operations to make at least k elements peaks in a circular array.

        :param nums: A list of integers representing the circular array.
        :param k: The target number of peaks to achieve.
        :return: The minimum number of operations required, or -1 if impossible.
        """
        n = len(nums)
        if k == 0:
            return 0

        if k > n // 2:
            return -1

        costs = [0] * n
        for i in range(n):
            leftNeighbor = nums[i - 1]
            rightNeighbor = nums[(i + 1) % n]
            maxNeighbor = leftNeighbor if leftNeighbor > rightNeighbor else rightNeighbor
            operationsNeeded = maxNeighbor + 1 - nums[i]
            costs[i] = operationsNeeded if operationsNeeded > 0 else 0

        def solve(arr: list[int], req: int) -> int:
            if req == 0:
                return 0

            m = len(arr)
            if req > (m + 1) // 2:
                return int(float('inf'))

            infVal = float('inf')
            prevTwo = [infVal] * (req + 1)
            prevOne = [infVal] * (req + 1)
            prevTwo[0] = 0
            prevOne[0] = 0

            if m > 0:
                prevOne[1] = arr[0]

            for i in range(1, m):
                curr = [infVal] * (req + 1)
                curr[0] = 0
                limit = min(req, (i + 2) // 2)
                val = arr[i]

                curr[1:limit + 1] = [
                    a if a < b + val else b + val
                    for a, b in zip(prevOne[1:limit + 1], prevTwo[:limit])
                ]

                prevTwo = prevOne
                prevOne = curr

            return int(prevOne[req])

        ansOne = solve(costs[1:], k)
        ansTwo = costs[0] + solve(costs[2:n - 1], k - 1)

        minOperationsAns = ansOne if ansOne < ansTwo else ansTwo

        return minOperationsAns if minOperationsAns < float('inf') else -1