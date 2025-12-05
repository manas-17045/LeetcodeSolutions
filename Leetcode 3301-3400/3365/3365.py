# Leetcode 3365: Rearrange K Substrings to Form Target String
# https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/
# Solved on 5th of December. 2025
from collections import Counter


class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        """
        Determines if string `s` can be rearranged into string `t` by splitting both into `k` equal-length substrings
        and checking if the counts of these substrings are identical.
        :param s: The source string.
        :param t: The target string.
        :param k: The number of substrings to split `s` and `t` into.
        :return: True if `s` can be rearranged into `t`, False otherwise.
        """
        segmentLength = len(s) // k
        sSegments = Counter(s[i: i + segmentLength] for i in range(0, len(s), segmentLength))
        tSegments = Counter(t[i: i + segmentLength] for i in range(0, len(t), segmentLength))
        return sSegments == tSegments