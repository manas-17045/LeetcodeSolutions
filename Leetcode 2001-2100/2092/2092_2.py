# Leetcode 2092: Find All People With Secret
# https://leetcode.com/problems/find-all-people-with-secret/
# Solved on 7th of August, 2025
class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        """
        Finds all people who eventually know the secret.

        Args:
            n: The total number of people.
            meetings: A list of meetings, where each meeting is [person1, person2, time].
            firstPerson: The first person (other than person 0) who knows the secret initially.

        Returns:
            A list of integers representing the people who know the secret.
        """
        # Initially, person 0 and firstPerson know the secret
        known = {0, firstPerson}

        # Sort meetings by time
        meetings.sort(key=lambda x: x[2])
        m = len(meetings)
        i = 0

        while i < m:
            t = meetings[i][2]
            # Gather all meetings at time t
            j = i
            participants = set()
            while j < m and meetings[j][2] == t:
                u, v, _ = meetings[j]
                participants.add(u)
                participants.add(v)
                j += 1

            # Build a local DSU among these participants
            parent = {p: p for p in participants}
            size = {p: 1 for p in participants}

            def find(x):
                # Path compression
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x
            
            def union(x, y):
                rx, ry = find(x), find(y)
                if rx == ry:
                    return
                # Union by size
                if size[rx] < size[ry]:
                    rx, ry = ry, rx
                parent[ry] = rx
                size[rx] += size[ry]

            # Union all meetings at this time
            for k in range(i, j):
                u, v, _ = meetings[k]
                union(u, v)

            # Find which local components have at least one known member
            seed_roots = {find(p) for p in participants if p in known}

            # Anyone in those components learns the secret
            for p in participants:
                if find(p) in seed_roots:
                    known.add(p)

            # Move to next time
            i = j

        # Return all people who know the secret
        return list(known)