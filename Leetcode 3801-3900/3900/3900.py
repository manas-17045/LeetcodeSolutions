# Leetcode 3900: Longest Balanced Substring After One Swap
# https://leetcode.com/problems/longest-balanced-substring-after-one-swap/
# Solved on 27th of April, 2026
import collections


class Solution:
    def longestBalanced(self, s: str) -> int:
        """
        Finds the length of the longest balanced substring possible after at most one swap.

        :param s: A string consisting of '0's and '1's.
        :return: The length of the longest balanced substring.
        """
        countZero = s.count('0')
        countOne = len(s) - countZero
        maxPossible = 2 * min(countZero, countOne)

        if maxPossible == 0:
            return 0

        maxLength = 0
        currentSum = 0
        prefixIndices = collections.defaultdict(collections.deque)
        prefixIndices[0].append(-1)

        for i in range(len(s)):
            if s[i] == '1':
                currentSum += 1
            else:
                currentSum -= 1

            for target in (currentSum, currentSum - 2, currentSum + 2):
                if target in prefixIndices:
                    targetDeque = prefixIndices[target]
                    while targetDeque and targetDeque[0] < i - maxPossible:
                        targetDeque.popleft()
                    if targetDeque:
                        currentLength = i - targetDeque[0]
                        if currentLength > maxLength:
                            maxLength = currentLength

            prefixIndices[currentSum].append(i)

        return maxLength