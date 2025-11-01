# Leetcode 3254: Find the Power of K-Size Subarrays I
# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/
# Solved on 1st of November, 2025
class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        """
        Calculates the "power" of k-size subarrays.

        For each subarray of size k, if it is consecutive and sorted (e.g., [1, 2, 3]),
        its power is the maximum element in that subarray. Otherwise, its power is -1.
        :param nums: A list of integers.
        :param k: The size of the subarrays.
        :return: A list of integers representing the power of each k-size subarray.
        """
        n = len(nums)
        results = []

        for i in range(n - k + 1):
            isConsecutiveAndSorted = True

            for j in range(1, k):
                currentIndex = i + j
                previousIndex = i + j - 1

                if nums[currentIndex] != nums[previousIndex] + 1:
                    isConsecutiveAndSorted = False
                    break

            if isConsecutiveAndSorted:
                maxElement = nums[i + k - 1]
                results.append(maxElement)
            else:
                results.append(-1)

        return results