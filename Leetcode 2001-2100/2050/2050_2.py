# Leetcode 20250: Parallel Courses III
# https://leetcode.com/problems/parallel-courses-iii/
# Solved on 27th of May. 2025
from collections import deque


class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        """
        Calculates the minimum time to complete all courses given the course dependencies and durations.

        Args:
            n: The total number of courses.
            relations: A list of lists representing the course dependencies, where relations[i] = [prevCourse, nextCourse]
                       indicates that nextCourse can only be taken after prevCourse is completed.
            time: A list of integers representing the time required to complete each course. time[i] is the time for course i+1.

        Returns:
            The minimum time required to complete all courses.

        Uses topological sort and dynamic programming to find the maximum time taken along any path in the course dependency graph.
        """
        # Build graph and indegree
        adj = [[] for _ in range(n + 1)]
        indegree = [0] * (n + 1)
        for u, v in relations:
            adj[u].append(v)
            indegree[v] += 1

        # dp[i] = minimum time to finish course i (including its own duration)
        dp = [0] * (n + 1)
        # Initialize dp with the time to take each course
        for i in range(1, n + 1):
            dp[i] = time[i - 1]

        # Start with all courses that have no prerequisites
        q = deque(i for i in range(1, n + 1) if indegree[i] == 0)

        # Process in topological order
        while q:
            u = q.popleft()
            for v in adj[u]:
                # You can start v only after finishing u,
                # so total time to finish v is max over all its predecessor
                dp[v] = max(dp[v], dp[u] + time[v - 1])
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        # The answer is the time by which the last course completes
        return max(dp[1:])