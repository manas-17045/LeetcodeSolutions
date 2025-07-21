# Leetcode 2940: Find Building Where Alice and Bob Can Meet
# https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/
# Solved on 22nd of December, 2024
class Solution:
    def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        """
        For each query (x, y), find the index of the leftmost building that is taller than both heights[x] and heights[y],
        and is located to the right of max(x, y).
        :param heights: A list of integers representing the heights of buildings.
        :param queries: A list of lists, where each inner list [x, y] represents a query.
        :return: A list of integers, where each element is the answer to the corresponding query.
        """
        n = len(heights)
        q = len(queries)

        # Build list of queries
        indexed = []
        for i, (x, y) in enumerate(queries):
            a, b = min(x, y), max(x, y)
            indexed.append((b, a, i))
        # Sort by b descending
        indexed.sort(key=lambda t: t[0], reverse=True)

        ans = [-1] * q
        stack = []
        hi = n - 1

        def last_greater(stack: list[int], target_h: int) -> int:
            l, r = -1, len(stack) - 1
            while l < r:
                m = (l + r + 1) // 2
                if heights[stack[m]] > target_h:
                    l = m
                else:
                    r = m - 1
            return l

        for b, a, qi in indexed:
            if a == b or heights[a] < heights[b]:
                ans[qi] = b
                continue

            while hi > b:
                while stack and heights[stack[-1]] <= heights[hi]:
                    stack.pop()
                stack.append(hi)
                hi -= 1

            m = last_greater(stack, heights[a])
            if m != -1:
                ans[qi] = stack[m]

        return ans