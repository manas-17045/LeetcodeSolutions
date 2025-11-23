# Leetcode 3695: Maximize Alternating Sum Using Swaps
# https://leetcode.com/problems/maximize-alternating-sum-using-swaps/
# Solved on 23rd of November, 2025
class Solution:
    def maxAlternatingSum(self, nums: list[int], swaps: list[list[int]]) -> int:
        """
        Maximizes the alternating sum of an array by performing a given set of swaps.

        The alternating sum is defined as nums[0] - nums[1] + nums[2] - nums[3] ...
        Swaps can be performed between elements that are in the same connected component.

        Args:
            nums: A list of integers representing the array.
            swaps: A list of pairs of indices representing allowed swaps.
        Returns:
            The maximum possible alternating sum after performing swaps.
        """

        size = len(nums)
        parent = list(range(size))

        def find(index):
            root = index
            while parent[root] != root:
                root = parent[root]
            while index != root:
                nextIndex = parent[index]
                parent[index] = root
                index = nextIndex
            return root

        def union(index1, index2):
            root1 = find(index1)
            root2 = find(index2)
            if root1 != root2:
                parent[root1] = root2

        for u, v in swaps:
            union(u, v)

        componentData = {}
        for i in range(size):
            root = find(i)
            if root not in componentData:
                componentData[root] = [[], 0]

            componentData[root][0].append(nums[i])
            if i % 2 == 0:
                componentData[root][1] += 1

        maxSum = 0
        for root in componentData:
            values = componentData[root][0]
            evenCount = componentData[root][1]

            values.sort(reverse=True)

            maxSum += sum(values[:evenCount])
            maxSum -= sum(values[evenCount:])

        return maxSum