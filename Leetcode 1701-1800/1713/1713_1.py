# Leetcode 1713: Minimum Operations to Make a Subsequence
# https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/
# Solved on 16th of June, 2025
import bisect


class Solution:
    def minOperations(self, target: list[int], arr: list[int]) -> int:
        """
        Given two arrays, target and arr, return the minimum number of operations
        needed to make target a subsequence of arr.
        An operation consists of inserting an element at any position in arr.

        The problem can be reduced to finding the length of the longest common subsequence
        between target and arr. The minimum number of operations is then the length of
        target minus the length of the longest common subsequence. Since target has no
        duplicate elements, this is equivalent to finding the longest increasing subsequence
        of the indices of the elements of arr that are present in target.
        """
        targetIndices = {value: idx for idx, value in enumerate(target)}

        stream = []
        for number in arr:
            if number in targetIndices:
                stream.append(targetIndices[number])

        if not stream:
            return len(target)

        lis = []
        for indexValue in stream:
            pos = bisect.bisect_left(lis, indexValue)
            if pos == len(lis):
                lis.append(indexValue)
            else:
                lis[pos] = indexValue

        return len(target) - len(lis)