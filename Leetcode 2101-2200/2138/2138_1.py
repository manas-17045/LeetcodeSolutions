# Leetcode 2138: Divide a String Into Groups of Size k
# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/
# Solved on 22nd of June, 2025
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        """
        Divides a string `s` into groups of size `k`.
        If the last group is incomplete, it is padded with the `fill` character.

        :param s: The input string.
        :param k: The desired group size.
        :param fill: The character to use for padding.
        :return: A list of strings, where each string is a group of size `k`.
        """
        n = len(s)
        result = []

        for i in range(0, n, k):
            currentGroup = s[i:(i + k)]

            if len(currentGroup) < k:
                paddingSize = k - len(currentGroup)
                currentGroup = currentGroup + fill * paddingSize

            result.append(currentGroup)

        return result