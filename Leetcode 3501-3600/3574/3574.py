# Leetcode 3574: Maximize Subarray GCD Score
# https://leetcode.com/problems/maximize-subarray-gcd-score/
# Solved on 6th of December, 2025
import math


class Solution:
    def maxGCDScore(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum possible GCD score of a subarray.

        Args:
            nums: A list of integers.
            k: An integer representing the maximum allowed cost.

        Returns:
            The maximum possible GCD score.
        """
        n = len(nums)
        maxScore = 0

        for i in range(n):
            if (n - i) * nums[i] * 2 <= maxScore:
                continue

            currG = nums[i]
            cost = 1

            currScore = currG
            if cost <= k:
                currScore *= 2
            if currScore > maxScore:
                maxScore = currScore

            for j in range(i + 1, n):
                val = nums[j]

                if val % currG != 0:
                    newG = math.gcd(currG, val)
                    ratio = currG // newG
                    if ratio % 2 == 0:
                        cost = 0
                    currG = newG

                if (n - i) * currG * 2 <= maxScore:
                    break

                if (val // currG) % 2 == 1:
                    cost += 1

                currLen = j - i + 1
                score = currLen * currG
                if cost <= k:
                    score *= 2

                if score > maxScore:
                    maxScore = score

        return maxScore