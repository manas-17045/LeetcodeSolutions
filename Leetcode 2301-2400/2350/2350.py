# Leetcode 2350: Shortest Impossible Sequence of Rolls
# https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/
# Solved on 11th of December, 2025
class Solution:
    def shortestSequence(self, rolls: list[int], k: int) -> int:
        """
        Calculates the length of the shortest impossible sequence of rolls.

        Args:
            rolls: A list of integers representing the sequence of rolls.
            k: An integer representing the number of faces on the die.
        Returns:
            An integer representing the length of the shortest impossible sequence.
        """
        sequenceLength = 1
        seenNumbers = set()

        for roll in rolls:
            seenNumbers.add(roll)

            if len(seenNumbers) == k:
                sequenceLength += 1
                seenNumbers.clear()

        return sequenceLength