# Leetcode 757: Set Intersection Size At Least Two
# https://leetcode.com/problems/set-intersection-size-at-least-two/
# Solved on 20th of November, 2025
class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        """
        Finds the minimum size of a set S such that for every interval `[a, b]` in `intervals`,
        the intersection of S with `[a, b]` has a size of at least 2.

        Args:
            intervals: A list of intervals, where each interval `[a, b]` is represented as `[start, end]`.

        Returns:
            The minimum size of the set S.
        """
        intervals.sort(key=lambda x: (x[1], -x[0]))

        setCount = 0
        secondHighest = -1
        highest = -1

        for start, end in intervals:
            if start > highest:
                setCount += 2
                secondHighest = end - 1
                highest = end
            elif start > secondHighest:
                setCount += 1
                secondHighest = highest
                highest = end

        return setCount