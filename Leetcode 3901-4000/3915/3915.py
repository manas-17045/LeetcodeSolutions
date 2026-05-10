# Leetcode 3915: Maximum Sum of Alternating Subsequence With Distance at Least K
# https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/
# Solved on 10th of May, 2026
class Solution:
    def maxAlternatingSum(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum sum of an alternating subsequence where each subsequent
        element has a distance of at least k from the previous element in the original array.

        :param nums: List of integers representing the input sequence.
        :param k: Minimum index distance required between consecutive elements in the subsequence.
        :return: The maximum possible sum of such an alternating subsequence.
        """
        maxVal = 100005
        treeZero = [0] * maxVal
        treeOne = [0] * maxVal
        n = len(nums)
        dpZero = [0] * n
        dpOne = [0] * n
        maxScore = 0

        for i in range(n):
            if i - k >= 0:
                pastVal = nums[i - k]

                valZero = dpZero[i - k]
                idxZero = maxVal - pastVal
                while idxZero < maxVal:
                    if valZero > treeZero[idxZero]:
                        treeZero[idxZero] = valZero
                    idxZero += idxZero & (-idxZero)

                valOne = dpOne[i - k]
                idxOne = pastVal
                while idxOne < maxVal:
                    if valOne > treeOne[idxOne]:
                        treeOne[idxOne] = valOne
                    idxOne += idxOne & (-idxOne)

            v = nums[i]

            bestOne = 0
            idxOneQ = v - 1
            while idxOneQ > 0:
                if treeOne[idxOneQ] > bestOne:
                    bestOne = treeOne[idxOneQ]
                idxOneQ -= idxOneQ & (-idxOneQ)
            dpZero[i] = bestOne + v

            bestZero = 0
            idxZeroQ = maxVal - v - 1
            while idxZeroQ > 0:
                if treeZero[idxZeroQ] > bestZero:
                    bestZero = treeZero[idxZeroQ]
                idxZeroQ -= idxZeroQ & (-idxZeroQ)
            dpOne[i] = bestZero + v

            if dpZero[i] > maxScore:
                maxScore = dpZero[i]
            if dpOne[i] > maxScore:
                maxScore = dpOne[i]

        return maxScore