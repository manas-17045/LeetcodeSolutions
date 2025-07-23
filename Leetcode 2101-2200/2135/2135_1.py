# Leetcode 2135: Count Words Obtained After Adding a Letter
# https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/
# Solved on 23rd of July, 2025
class Solution:
    def wordCount(self, startWords: list[str], targetWords: list[str]) -> int:
        """
        Counts how many target words can be formed by adding exactly one letter to a start word.

        Args:
            startWords (list[str]): A list of starting words.
            targetWords (list[str]): A list of target words.
        Returns:
            int: The number of target words that can be obtained.
        """
        startWordMasks = set()
        for word in startWords:
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord('a'))
            startWordMasks.add(mask)

        count = 0
        for word in targetWords:
            targetMask = 0
            for char in word:
                targetMask |= 1 << (ord(char) - ord('a'))

            for char in word:
                potentialStartMask = targetMask ^ (1 << (ord(char) - ord('a')))
                if potentialStartMask in startWordMasks:
                    count += 1
                    break

        return count