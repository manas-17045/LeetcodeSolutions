# Leetcode 3085: Minimum Deletions to Make String K-Special
# https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/
# Solved on 21st of June, 2025
import collections


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        """
        Calculates the minimum number of deletions required to make the given word k-special.

        A string is k-special if the difference between the maximum and minimum frequencies
        of its characters is at most k.

        The approach iterates through all possible target minimum frequencies. For each
        target minimum frequency, it calculates the deletions needed:
        - Characters with frequency less than the target minimum are fully deleted.
        - Characters with frequency greater than (target minimum + k) are reduced to
          (target minimum + k).

        Args:
            word (str): The input string.
            k (int): The maximum allowed difference between max and min frequencies.
        """
        if not word:
            return 0

        countsMap = collections.Counter(word)
        freqs = list(countsMap.values())

        # Determine the maximum frequency observed in the original string.
        maxObservedFreq = 0
        if freqs:
            for fVal in freqs:
                if fVal > maxObservedFreq:
                    maxObservedFreq = fVal

        # Initialize with worst-case (delete all chars)
        minTotalDeletions = len(word)

        # Iterate through all possible values for the minimum frequency (currentMinFreqTarget)
        # that characters could have in the final k-special string.
        for currentMinFreqTarget in range(maxObservedFreq + 1):
            currentDeletionsForThisTarget = 0

            for originalFreq in freqs:
                if originalFreq < currentMinFreqTarget:
                    currentDeletionsForThisTarget += originalFreq
                elif originalFreq > currentMinFreqTarget + k:
                    currentDeletionsForThisTarget += originalFreq - (currentMinFreqTarget + k)

            if currentDeletionsForThisTarget < minTotalDeletions:
                minTotalDeletions = currentDeletionsForThisTarget

        return minTotalDeletions