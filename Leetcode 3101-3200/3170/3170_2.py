# Leetcode 3170: Lexicographically Minimum String After Removing Stars
# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/
# Solved on 7th of June, 2025
import heapq


class Solution:
    def clearStars(self, s: str) -> str:
        """
        Clears stars from a string by removing the smallest character to the left of each star.

        Args:
            s: The input string containing lowercase English letters and stars.

        Returns:
            The string after clearing all stars and their corresponding characters.
        """
        heap = []
        deleted = []
        letters = []
        letterId = 0

        for ch in s:
            if ch == '*':
                # Remove one smallest letter seen so far
                c, negId = heapq.heappop(heap)
                deleted[-negId] = True
            else:
                # It's a letter: record it, give it an ID, push to heap
                letters.append(ch)
                deleted.append(False)
                heapq.heappush(heap, (ch, -letterId))
                letterId += 1

        # Rebuild the answer from all non-deleted letters, in original order
        out = []
        for idx, ch in enumerate(letters):
            if not deleted[idx]:
                out.append(ch)
        return "".join(out)