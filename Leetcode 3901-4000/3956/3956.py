# Leetcode 3956: Maximum Sum of M Non-Overlapping Subarrays I
# https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-i/
# Solved on 25th of June, 2026
import collections


class Solution:
    def maximumSum(self, nums: list[int], m: int, l: int, r: int) -> int:
        """
        Computes the maximum sum of m non-overlapping subarrays of length between l and r.
        
        :param nums: The input array.
        :param m: The number of subarrays.
        :param l: The minimum length of a subarray.
        :param r: The maximum length of a subarray.
        :return: The maximum sum of m non-overlapping subarrays.
        """
        n = len(nums)
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]
        
        prevDp = [0] * (n + 1)
        maxAns = float('-inf')

        for c in range(1, m + 1):
            currDp = [float('-inf')] * (n + 1)
            dq = collections.deque()

            for i in range(l, n + 1):
                currJ = i - l

                if prevDp[currJ] != float('-inf'):
                    val = prevDp[currJ] - prefixSum[currJ]
                    while dq and dq[-1][1] <= val:
                        dq.pop()
                    dq.append((currJ, val))

                while dq and dq[0][0] < i - r:
                    dq.popleft()

                currDp[i] = currDp[i - 1]

                if dq:
                    currDp[i] = max(currDp[i], prefixSum[i] + dq[0][1])

            maxAns = max(maxAns, currDp[n])
            prevDp = currDp

        return int(maxAns)