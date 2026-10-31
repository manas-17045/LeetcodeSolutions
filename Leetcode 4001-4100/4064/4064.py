# Leetcode 4064: Longest Subarray Divisible by K with At Most One Negation II
# https://leetcode.com/problems/longest-subarray-divisible-by-k-with-at-most-one-negation-ii/
# Solved on 31st of October, 2026
class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        """
        Finds the length of the longest subarray that can become divisible by k 
        with at most one negation.
        
        Args:
            nums (list[int]): An array of integers.
            k (int): The divisor.
            
        Returns:
            int: The maximum length of a valid subarray.
        """
        inf = 10**9
        firstP = [inf] * k
        minIForR = [inf] * k
        processedXLen = [0] * k
        seenX = []

        maxLen = 0
        pSum = 0

        for j in range(len(nums)):
            currX = pSum % k

            if firstP[currX] == inf:
                firstP[currX] = j
                seenX.append(currX)
                if j < minIForR[currX]:
                    minIForR[currX] = j

            v = (2 * nums[j]) % k

            for idx in range(processedXLen[v], len(seenX)):
                x = seenX[idx]
                r = (x + v) % k
                if firstP[x] < minIForR[r]:
                    minIForR[r] = firstP[x]

            processedXLen[v] = len(seenX)

            pSum += nums[j]
            rTarget = pSum % k

            if minIForR[rTarget] != inf:
                currentLen = j + 1 - minIForR[rTarget]
                if currentLen > maxLen:
                    maxLen = currentLen

        return maxLen