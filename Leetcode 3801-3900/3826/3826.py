# Leetcode 3826: Minimum Partition Score
# https://leetcode.com/problems/minimum-partition-score/
# Solved on 7th of February, 2026
class Solution:
    def minPartitionScore(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum partition score by dividing the array into k non-empty subarrays.

        :param nums: List of integers representing the array to be partitioned.
        :param k: Integer representing the number of partitions.
        :return: Integer representing the minimum total score.
        """
        n = len(nums)
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            val = prefixSum[i]
            dp[i] = val * (val + 1) // 2

        def compute(prevDp, nextDp, left, right, optL, optR):
            if left > right:
                return

            mid = (left + right) // 2
            minScore = float('inf')
            bestSplit = -1

            limit = min(mid - 1, optR)

            for i in range(optL, limit + 1):
                val = prefixSum[mid] - prefixSum[i]
                currentScore = prevDp[i] + val * (val + 1) // 2
                if currentScore < minScore:
                    minScore = currentScore
                    bestSplit = i

            nextDp[mid] = minScore

            compute(prevDp, nextDp, left, mid - 1, optL, bestSplit)
            compute(prevDp, nextDp, mid + 1, right, bestSplit, optR)

        for i in range(2, k + 1):
            nextDp = [0] * (n + 1)
            compute(dp, nextDp, i, n, i - 1, n - 1)
            dp = nextDp

        return dp[n]