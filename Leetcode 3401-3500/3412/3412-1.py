# Leetcode 3412: Find Mirror Score of a String
# https://leetcode.com/problems/find-mirror-score-of-a-string/
# Solved on 18th of September, 2025
import collections


class Solution:
    def calculateScore(self, s: str) -> int:

        totalScore = 0
        unmarkedIndices = collections.defaultdict(list)

        for i, char in enumerate(s):
            mirrorChar = chr(ord('a') + ord('z') - ord(char))

            if unmarkedIndices[mirrorChar]:
                j = unmarkedIndices[mirrorChar].pop()
                totalScore += i - j
            else:
                unmarkedIndices[char].append(i)

        return totalScore