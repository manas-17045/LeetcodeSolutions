# Leetcode 20250: Parallel Courses III
# https://leetcode.com/problems/parallel-courses-iii/
# Solved on 27th of May, 2025
import collections


class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        """
        Calculates the minimum time to complete all courses given their dependencies and durations.

        This problem can be modeled as finding the longest path in a Directed Acyclic Graph (DAG),
        where nodes are courses and edges represent prerequisites. The weight of each node is the
        time required to complete that course.

        The algorithm uses Kahn's algorithm (topological sort) combined with dynamic programming
        to track the earliest completion time for each course.

        Args:
            n: The total number of courses (1 to n).
            relations: A list of prerequisite pairs [prevCourse, nextCourse].
            time: A list where time[i] is the duration of course i + 1.
        """
        # adj[u] stores list of courses for which u is a prerequisite
        # Courses are 1-indexed, so course IDs range from 1 to n
        adj = collections.defaultdict(list)

        # in_degree[i] stores number of prerequisites for course i.
        # Using (n + 1) size for 1-based indexing(index 0 unused).
        in_degree = [0] * (n + 1)

        for prev_course, next_course in relations:
            # Edge from prev_course to next_course
            adj[prev_course].append(next_course)
            in_degree[next_course] += 1

        # dist[i] stores the earliest time course i can be completed.
        # Using (n + 1) size for 1-based indexing.
        # Initialized to 0. For source nodes (in_degree == 0), it's set to their own time.
        # For other nodes, it's updated based on prerequisite completion time.
        dist = [0] * (n + 1)

        queue = collections.deque()

        # Initialize queue with courses having no r=prerequisites (in-degree 0)
        for i in range(1, n + 1):   # Course IDs are 1 to n
            if in_degree[i] == 0:
                queue.append(i)
                # For these courses, completion time is their own duration,
                # as they can start at time 0.
                # time array is 0-indexed: time[i-1] is duration for course i.
                dist[i] = time[i - 1]

        # max_total_time will track the maximum completion time among all courses.
        # This is the final answer, as all courses must be completed.
        max_total_time = 0

        while queue:
            # u is a course whose prerequisites are met and dist[u] is calculated.
            u = queue.popleft()

            # The completion time of u is dist[u].
            # This is a candidate for the overall minimum time to complete all courses
            # (i.e., if u is one of the last courses to finish).
            max_total_time = max(max_total_time, dist[u])

            # For each course v that has u as a prerequisite
            for v in adj[u]:
                # Update completion time for v.
                # v can only start after u is completed (at time dist[u]).
                # So, v would finish at dist[u] + time[v-1] (duration of v).
                # We take max with existing dist[v] because v might have other prerequisites,
                # and it must wait for the one that finishes latest.
                # This ensures dist[v] correctly represents:
                # (max completion_time of prerequisite p) + time[v-1].
                dist[v] = max(dist[v], dist[u] + time[v - 1])

                in_degree[v] -= 1
                # If all prerequisites for v are now met (in_degree[v] is 0),
                # v's earliest start time component of dist[v] is determined.
                # Add v to the queue for processing its dependent courses.
                if in_degree[v] == 0:
                    queue.append(v)

        # max_total_time will hold the time when the "slowest" path of courses finishes.
        return max_total_time