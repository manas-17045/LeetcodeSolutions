# Leetcode 2767: Partition String Into Minimum Beautiful Substrings
# https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/
# Solved on 17th of October, 2025
class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        """
        Partitions a binary string into the minimum number of "beautiful" substrings.
        A beautiful substring is a binary representation of a power of 5.
        :param s: The input binary string.
        :return: The minimum number of beautiful substrings, or -1 if no such partition exists.
        """
        beautifulNumbers = {
            '1', '101', '11001', '1111101', '1001110001',
            '110000110101', '11110100001001'
        }

        strLen = len(s)
        dp = [float('inf')] * (strLen + 1)
        dp[0] = 0

        for i in range(1, strLen + 1):
            for beautifulNum in beautifulNumbers:
                beautifulLen = len(beautifulNum)
                if i >= beautifulLen and s[i - beautifulLen:i] == beautifulNum:
                    if dp[i - beautifulLen] != float('inf'):
                        dp[i] = min(dp[i], dp[i - beautifulLen] + 1)

        finalResult = dp[strLen]
        return int(finalResult) if finalResult != float('inf') else -1