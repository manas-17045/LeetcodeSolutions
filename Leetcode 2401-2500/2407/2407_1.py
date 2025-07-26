# Leetcode 2407: Longest Increasing Subsequence II
# https://leetcode.com/problems/longest-increasing-subsequence-ii/
# Solved on 26th of July, 2025
class Solution:
    def lengthOfLIS(self, nums: list[int], k: int) -> int:
        """
        Calculates the length of the longest increasing subsequence (LIS) such that the difference
        between adjacent elements in the subsequence is at most k.

        :param nums: A list of integers.
        :param k: The maximum allowed difference between adjacent elements in the LIS.
        :return: The length of the longest increasing subsequence.
        """
        valueRange = 100001
        tree = [0] * (2 * valueRange)

        def update(index: int, value: int):
            pos = index + valueRange
            tree[pos] = value
            while pos > 1:
                pos //= 2
                tree[pos] = max(tree[pos * 2], tree[pos * 2 + 1])

        def query(left: int, right: int) -> int:
            left += valueRange
            right += valueRange
            result = 0
            while left < right:
                if left % 2 == 1:
                    result = max(result, tree[left])
                    left += 1
                if right % 2 == 1:
                    right -= 1
                    result = max(result, tree[right])
                left //= 2
                right //= 2
            return result

        maxLength = 0
        for num in nums:
            startRange = max(1, num - k)
            prevLength = query(startRange, num)

            currentLength = prevLength + 1
            update(num, currentLength)
            maxLength = max(maxLength, currentLength)

        return maxLength