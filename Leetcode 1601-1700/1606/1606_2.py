# Leetcode 1606: Find Servers That Handled Most Number of Requests
# https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/
# Solved on 5th of July, 2025
import bisect
import heapq


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        """
        Calculates the busiest servers based on a sequence of incoming requests.

        Args:
            k (int): The number of available servers.
            arrival (list[int]): A list of arrival times for each request.
            load (list[int]): A list of processing loads (durations) for each request.

        Returns:
            list[int]: A list of server IDs that handled the maximum number of requests.

        The algorithm simulates the request handling process, managing server availability
        using a min-heap for busy servers and a sorted list for available servers.
        """
        # counts[i] = number of requests handled by server i
        counts = [0] * k

        # min-heap of (free_time, server_id)
        busy = []

        # Sorted list of available server IDs
        avail = list(range(k))

        for i, (t, l) in enumerate(zip(arrival, load)):
            # Free up any servers that have finished by time t
            while busy and busy[0][0] <= t:
                free_time, srv = heapq.heappop(busy)
                # Put srv back into avail in sorted order
                bisect.insort(avail, srv)

            if not avail:
                # All servers busy -> drop this request
                continue

            # Choose server id >= (i mod k), wrap around
            start = i % k
            idx = bisect.bisect_left(avail, start)
            if idx == len(avail):
                idx = 0
            srv = avail.pop(idx)

            # Assign request -> srv will be busy until t + 1
            counts[srv] += 1
            heapq.heappush(busy, ((t + 1), srv))

        # Find the max count and return all servers achieving it
        mx = max(counts)
        return [i for i, c in enumerate(counts) if c == mx]