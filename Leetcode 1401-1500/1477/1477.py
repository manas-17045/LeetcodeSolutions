# Leetcode 1477: Find Two Non-overlapping Sub-arrays Each With Target Sum
# https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/
# Solved on 17th of September, 2026
class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        """
        Finds the minimum sum of lengths of two non-overlapping sub-arrays
        with sums equal to the target.

        Parameters:
        arr (list[int]): A list of positive integers.
        target (int): The target sum to match.

        Returns:
        int: The minimum combined length of two matching sub-arrays, or -1 if impossible.
        """
        arrLen = len(arr)
        minLens = [float('inf')] * arrLen
        minTotalLen = float('inf')
        currSum = 0
        leftPtr = 0

        for rightPtr in range(arrLen):
            currSum += arr[rightPtr]

            while currSum > target and leftPtr <= rightPtr:
                currSum -= arr[leftPtr]
                leftPtr += 1
            
            if currSum == target:
                subLen = rightPtr - leftPtr + 1
                if leftPtr > 0 and minLens[leftPtr - 1] != float('inf'):
                    minTotalLen = min(minTotalLen, subLen + minLens[leftPtr - 1])
                if rightPtr > 0:
                    minLens[rightPtr] = min(minLens[rightPtr - 1], subLen)
                else:
                    minLens[rightPtr] = subLen
            else:
                if rightPtr > 0:
                    minLens[rightPtr] = minLens[rightPtr - 1]

        return minTotalLen if minTotalLen != float('inf') else -1