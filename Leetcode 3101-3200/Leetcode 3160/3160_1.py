# Leetcode 3160: Find the Number of Distinct Colors Among the Balls
# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        """
        Simulates coloring balls and tracks the number of distinct colors after each query.

        Args:
            limit: An integer representing the maximum ball index (not used in the logic, but present in the problem statement).
            queries: A list of lists, where each inner list contains two integers: [ball_index, color].
                     This represents a query to color the ball at ball_index with the given color.

        Returns: A list of integers, where each integer represents the number of distinct colors after processing the
        corresponding query.
        """
        # Map each ball index to its current color
        ball_color = {}
        # Count of balls per color
        color_count = {}
        # Results after each query
        results = []

        for idx, color in queries:
            # If this ball was already colored, decrement its old color count
            if idx in ball_color:
                old_color = ball_color[idx]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    # No balls remain with that color
                    del color_count[old_color]

            # Assign the new color
            ball_color[idx] = color

            # Increment count for the new color
            color_count[color] = color_count.get(color, 0) + 1

            # Number of distinct colors is just the number of keys in color_count
            results.append(len(color_count))

        return results