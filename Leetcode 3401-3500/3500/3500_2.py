# Solved on 2nd of June, 2025

class Solution:
    def minimumCost(self, nums: list[int], cost: list[int], k: int) -> int:
        """
        Calculates the minimum cost to partition the array nums into segments.

        The cost of a partition is the sum of the costs of each segment.
        The cost of a segment from index j to i-1 is calculated as:
        (sum of nums[j...i-1]) * (sum of cost[j...i-1]) + k * (sum of cost[i...n-1])

        Args:
            nums: A list of integers.
            cost: A list of integers representing the cost associated with each element in nums.
            k: An integer penalty for each segment boundary.

        Returns:
            The minimum total cost to partition the array.
        """
        n = len(nums)

        # Prefix-sums of nums and cost
        preNum = [0] * (n + 1)
        preCost = [0] * (n + 1)
        for i in range(n + 1):
            preNum[i] = preNum[i - 1] + nums[i - 1]
            preCost[i] = preCost[i - 1] + cost[i - 1]

        totalCost = preCost[n]

        # dp[i] = minimum total cost to partition the prefix nums[0...(i - 1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            best = float('inf')
            for j in range(i):
                segmentCost = preNum[i] * (preCost[i] - preCost[j])
                boundaryPenalty = k * (totalCost - preCost[j])
                candidate = dp[j] + segmentCost + boundaryPenalty
                if candidate < best:
                    best = candidate
            dp[i] = best

        return int(dp[n])