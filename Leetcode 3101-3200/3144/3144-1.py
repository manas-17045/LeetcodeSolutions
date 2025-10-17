# Leetcode 3144: Minimum Substring Partition of Equal Character Frequency
# https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/
# Solved on 17th of October, 2025
import collections


class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        """
        Calculates the minimum number of substrings a given string `s` can be partitioned into,
        such that each substring has an equal character frequency.
        :param s: The input string.
        :return: The minimum number of partitions.
        """
        strLen = len(s)
        minPartitions = list(range(strLen + 1))

        for i in range(1, strLen + 1):
            freqMap = collections.defaultdict(int)
            for j in range(i - 1, -1, -1):
                freqMap[s[j]] += 1

                if len(set(freqMap.values())) == 1:
                    minPartitions[i] = min(minPartitions[i], minPartitions[j] + 1)

        return minPartitions[strLen]