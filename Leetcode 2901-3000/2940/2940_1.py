# Leetcode 2940: Find Building Where Alice and Bob Can Meet
# https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/
# Solved on 22nd of December, 2024
class Solution:
    def leftMostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        """
        Finds the leftmost building where Alice and Bob can meet for each query.
        Args:
            heights (list[int]): A list of integers representing the heights of buildings.
            queries (list[list[int]]): A list of queries, where each query is [a, b]
                                        representing Alice's and Bob's initial building indices.
        Returns:
            list[int]: A list of integers, where each element is the index of the leftmost building where Alice and Bob
                        can meet for the corresponding query, or -1 if they cannot meet.
        """
        indexed_queries = self.get_indexed_queries(queries)
        ans = [-1] * len(queries)
        stack = []

        heights_index = len(heights) - 1
        for indexed_query in indexed_queries:
            query_index = indexed_query.query_index
            a = indexed_query.a
            b = indexed_query.b
            if a == b or heights[a] < heights[b]:
                ans[query_index] = b
            else:
                while heights_index > b:
                    while stack and heights[stack[-1]] <= heights[heights_index]:
                        stack.pop()
                    stack.append(heights_index)
                    heights_index -= 1
                j = self.last_greater(stack, a, heights)
                if j != -1:
                    ans[query_index] = stack[j]

        return ans

    class IndexedQuery:
        def __init__(self, query_index, a, b):
            self.query_index = query_index
            self.a = a
            self.b = b

    def last_greater(self, A, target, heights):
        l, r = -1, len(A) - 1
        while l < r:
            m = (l + r + 1) // 2
            if heights[A[m]] > heights[target]:
                l = m
            else:
                r = m - 1
        return l

    def get_indexed_queries(self, queries):
        indexed_queries = []
        for i in range(len(queries)):
            a = min(queries[i][0], queries[i][1])
            b = max(queries[i][0], queries[i][1])
            indexed_queries.append(self.IndexedQuery(i, a, b))
        indexed_queries.sort(key=lambda x: x.b, reverse=True)
        return indexed_queries