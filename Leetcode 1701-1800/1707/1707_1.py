# Leetcode 1707: Maximum XOR With an Element From Array
# https://leetcode.com/problems/maximum-xor-with-an-element-from-array/
# Solved on 17th of August, 2025
class Solution:
    def maximizeXor(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        """
        Given an array nums and an array queries, where each query queries[i] = [xi, mi],
        return an array answer where answer[i] is the maximum bitwise XOR of xi with any
        element in nums that is less than or equal to mi. If no such element exists, the answer is -1.

        Args:
            nums: A list of integers.
            queries: A list of lists, where each inner list contains [xi, mi].
        Returns:
            A list of integers representing the maximum XOR for each query.
        """
        nums.sort()

        queriesWithIndex = []
        for i, q in enumerate(queries):
            queriesWithIndex.append((q[0], q[1], i))

        queriesWithIndex.sort(key=lambda x: x[1])

        answer = [-1] * len(queries)
        trieRoot = {}
        numsIndex = 0
        maxBit = 29

        for xi, mi, originalIndex in queriesWithIndex:
            while numsIndex < len(nums) and nums[numsIndex] <= mi:
                num = nums[numsIndex]
                node = trieRoot
                for i in range(maxBit, -1, -1):
                    bit = (num >> i) & 1
                    if bit not in node:
                        node[bit] = {}
                    node = node[bit]
                numsIndex += 1

            if not trieRoot:
                answer[originalIndex] = -1
                continue

            maxXor = 0
            node = trieRoot
            for i in range(maxBit, -1, -1):
                bit = (xi >> i) & 1
                oppositeBit = 1 - bit

                if oppositeBit in node:
                    maxXor |= (1 << i)
                    node = node[oppositeBit]
                else:
                    node = node[bit]

            answer[originalIndex] = maxXor

        return answer