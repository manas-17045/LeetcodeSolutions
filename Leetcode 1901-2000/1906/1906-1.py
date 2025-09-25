# Leetcode 1906: Minimum Absolute Difference Queries
# https://leetcode.com/problems/minimum-absolute-difference-queries/
# Solved on 25th of September, 2025
class Solution:
    def minDifference(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        """
        Calculates the minimum absolute difference between any two distinct elements
        within specified subarrays for multiple queries.

        Args:
            nums (list[int]): The input array of integers.
            queries (list[list[int]]): A list of queries, where each query is [left, right]
                                       representing a subarray nums[left...right].

        Returns:
            list[int]: A list of integers, where each element is the minimum absolute difference
                       for the corresponding query. If a subarray has fewer than two distinct
                       elements, -1 is returned for that query.
        """
        numsLength = len(nums)
        maxValue = 100
        prefixCounts = [[0] * (maxValue + 1) for _ in range(numsLength + 1)]

        # Precompute the counts of each number up to each index.
        for i in range(numsLength):
            # Copy counts fron the previous prefix.
            prefixCounts[i + 1] = prefixCounts[i][:]
            # Increment the count for the current number.
            prefixCounts[i + 1][nums[i]] += 1

        answer = []
        # Process each query using the precomputed counts.
        for leftIndex, rightIndex in queries:
            minDiff = float('inf')
            lastNum = -1

            # Check for the presence of each number from 1 to 100 in the subarray
            for num in range(1, maxValue + 1):
                countInRange = prefixCounts[rightIndex + 1][num] - prefixCounts[leftIndex][num]
                if countInRange > 0:
                    # If a previous number was found, calculate the difference.
                    if lastNum != -1:
                        minDiff = min(minDiff, num - lastNum)
                    lastNum = num

            # If minDiff was not updated, there are fewer than two distinct numbers.
            answer.append(-1 if minDiff == float('inf') else minDiff)

        return answer