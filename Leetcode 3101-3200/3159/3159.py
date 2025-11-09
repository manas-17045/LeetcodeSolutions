# Leetcode 3159: Find Occurrences of an Element in an Array
# https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/
# Solved on 9th of November, 2025
import collections


class Solution:
    def occurrencesOfElement(self, nums: list[int], queries: list[int], x: int) -> list[int]:
        """
        Finds the k-th occurrence of a specific element `x` in the `nums` array for each query.

        Args:
            nums (list[int]): The input array of integers.
            queries (list[int]): A list of integers, where each `k` in `queries` represents the k-th occurrence to find.
            x (int): The target element to find occurrences of.

        Returns:
            list[int]: A list of integers where each element is the 0-indexed position of the k-th occurrence of `x`, or -1 if the k-th occurrence does not exist.
        """
        elementIndices = collections.defaultdict(list)

        for index, num in enumerate(nums):
            elementIndices[num].append(index)

        answer = []
        indicesOfX = elementIndices.get(x, [])

        for k in queries:
            if k - 1 < len(indicesOfX):
                answer.append(indicesOfX[k - 1])
            else:
                answer.append(-1)

        return answer