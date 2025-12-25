# Leetcode 3780: Maximum Sum of Three Numbers Divisible by Three
# https://leetcode.com/problems/maximum-sum-of-three-numbers-divisible-by-three/
# Solved on 25th of December, 2025
class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of three numbers from the input list that is divisible by three.

        :param nums: A list of integers.
        :return: The maximum sum of three numbers divisible by three.
        """
        bucket0 = []
        bucket1 = []
        bucket2 = []

        for num in nums:
            if num % 3 == 0:
                bucket0.append(num)
                bucket0.sort(reverse=True)
                if len(bucket0) > 3:
                    bucket0.pop()
            elif num % 3 == 1:
                bucket1.append(num)
                bucket1.sort(reverse=True)
                if len(bucket1) > 3:
                    bucket1.pop()
            else:
                bucket2.append(num)
                bucket2.sort(reverse=True)
                if len(bucket2) > 3:
                    bucket2.pop()

        maxSum = 0

        if len(bucket0) == 3:
            maxSum = max(maxSum, sum(bucket0))
        if len(bucket1) == 3:
            maxSum = max(maxSum, sum(bucket1))
        if len(bucket2) == 3:
            maxSum = max(maxSum, sum(bucket2))
        if bucket0 and bucket1 and bucket2:
            maxSum = max(maxSum, bucket0[0] + bucket1[0] + bucket2[0])

        return maxSum
