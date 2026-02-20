# Leetcode 3845: Maximum Subarray XOR with Bounded Range
# https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/
# Solved on 20th of February, 2026
import collections


class Solution:
    def maxXor(self, nums: list[int], k: int) -> int:
        """
        Finds the maximum XOR sum of a subarray where the difference between
        the maximum and minimum elements of that subarray is at most k.

        :param nums: List of integers representing the input array.
        :param k: Integer representing the maximum allowed difference between max and min elements.
        :return: Integer representing the maximum XOR sum found.
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ nums[i]

        trieNode = [[0, 0]]
        trieCount = [0]

        def addNode(numVal):
            currNode = 0
            for i in range(14, -1, -1):
                bitVal = (numVal >> i) & 1
                if not trieNode[currNode][bitVal]:
                    trieNode.append([0, 0])
                    trieCount.append(0)
                    trieNode[currNode][bitVal] = len(trieNode) - 1

                currNode = trieNode[currNode][bitVal]
                trieCount[currNode] += 1

        def removeNode(numVal):
            currNode = 0
            for i in range(14, -1, -1):
                bitVal = (numVal >> i) & 1
                currNode = trieNode[currNode][bitVal]
                trieCount[currNode] -= 1

        def queryNode(numVal):
            currNode = 0
            maxResult = 0
            for i in range(14, -1, -1):
                bitVal = (numVal >> i) & 1
                targetBit = bitVal ^ 1
                if trieNode[currNode][targetBit] and trieCount[trieNode[currNode][targetBit]] > 0:
                    maxResult |= (1 << i)
                    currNode = trieNode[currNode][targetBit]
                else:
                    currNode = trieNode[currNode][bitVal]

            return maxResult

        maxDeque = collections.deque()
        minDeque = collections.deque()

        leftIdx = 0
        maxPossibleVal = 0

        for rightIdx in range(n):
            while maxDeque and nums[maxDeque[-1]] <= nums[rightIdx]:
                maxDeque.pop()
            maxDeque.append(rightIdx)

            while minDeque and nums[minDeque[-1]] >= nums[rightIdx]:
                minDeque.pop()
            minDeque.append(rightIdx)

            while nums[maxDeque[0]] - nums[minDeque[0]] > k:
                removeNode(prefix[leftIdx])
                leftIdx += 1
                if maxDeque[0] < leftIdx:
                    maxDeque.popleft()
                if minDeque[0] < leftIdx:
                    minDeque.popleft()

            addNode(prefix[rightIdx])
            maxPossibleVal = max(maxPossibleVal, queryNode(prefix[rightIdx + 1]))

        return maxPossibleVal