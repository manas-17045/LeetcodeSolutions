# Leetcode 1505: Minimum Possible Integer After at Most K Adjacent Swaps On Digits
# https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/
# Solved on 19th of June, 2025
import collections


class FenwickTree:
    def __init__(self, size: int):
        self.treeSize = size + 1
        self.tree = [0] * self.treeSize

    def update(self, index: int, delta: int):
        # index is 0-based for the user
        internalIndex = index + 1   # Convert to 1-basd for internal BIT logic
        while internalIndex < self.treeSize:
            self.tree[internalIndex] += delta
            internalIndex += internalIndex & (-internalIndex)   # Move to next relevant index

    def query(self, index: int) -> int:
        # Returns prefix sum up to and including index (0-based)
        if index < 0:   # Handles query for elements before the 0-th element
            return 0

        internalIndex = index + 1   # Convert to 1-based for internal BIT logic
        currentSum = 0
        while internalIndex > 0:
            currentSum += self.tree[internalIndex]
            internalIndex -= internalIndex & (-internalIndex)   # Move to previous relevant index
        return currentSum

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)

        digitOriginalIndices = [collections.deque() for _ in range(10)]
        for i, charDigit in enumerate(num):
            digitOriginalIndices[int(charDigit)].append(i)

        bit = FenwickTree(n)
        for i in range(n):
            bit.update(i, 1)

        resultChars = []
        isPicked = [False] * n

        for _ in range(n):
            if k == 0:
                break

            for dValue in range(10):
                if digitOriginalIndices[dValue]:
                    originalIdx = digitOriginalIndices[dValue][0]

                    costToMove = bit.query(originalIdx - 1)

                    if costToMove <= k:
                        resultChars.append(str(dValue))
                        k -= costToMove

                        bit.update(originalIdx, -1)
                        isPicked[originalIdx] = True
                        digitOriginalIndices[dValue].popleft()

                        break

        if len(resultChars) < n:
            for i in range(n):
                if not isPicked[i]:
                    resultChars.append(num[i])

        return "".join(resultChars)