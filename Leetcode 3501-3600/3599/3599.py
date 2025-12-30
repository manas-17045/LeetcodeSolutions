# Leetcode 3599: Partition Array to Minimize XOR
# https://leetcode.com/problems/partition-array-to-minimize-xor/
# Solved on 30th of December, 2025
class Solution:
    def minXor(self, nums: list[int], k: int) -> int:
        """
        Partitions the array `nums` into `k` non-empty subarrays such that the maximum XOR sum among all subarrays is minimized.

        Args:
            nums: A list of integers.
            k: The number of partitions.

        Returns:
            The minimum possible maximum XOR sum among all subarrays.
        """
        n = len(nums)
        prefixXor = [0] * (n + 1)
        for i in range(n):
            prefixXor[i + 1] = prefixXor[i] ^ nums[i]

        prevDp = [float('inf')] * (n + 1)
        prevDp[0] = 0

        for c in range(1, k + 1):
            currDp = [float('inf')] * (n + 1)
            for i in range(c, n + 1):
                currentMin = float('inf')
                for j in range(c - 1, i):
                    if prevDp[j] >= currentMin:
                        continue

                    xorSum = prefixXor[i] ^ prefixXor[j]
                    currentMax = prevDp[j] if prevDp[j] > xorSum else xorSum

                    if currentMax < currentMin:
                        currentMin = currentMax
                currDp[i] = currentMin
            prevDp = currDp

        return int(prevDp[n])