# Leetcode 2747: Count Zero Request Servers
# https://leetcode.com/problems/count-zero-request-servers/
# Solved on 10th of August, 2025
class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        """
        Counts the number of servers that have zero requests within a specific time window for each query.

        Args:
            n (int): The total number of servers, labeled from 1 to n.
            logs (list[list[int]]): A list of log entries, where each entry is [server_id, time].
            x (int): The duration of the time window for counting requests.
            queries (list[int]): A list of query times. For each query time `t`, we need to count servers with zero requests in the interval [t - x, t].

        Returns:
            list[int]: A list of integers, where the i-th element is the number of zero-request servers for the i-th query.
        """
        logs.sort(key=lambda item: item[1])

        indexedQueries = [[queries[i], i] for i in range(len(queries))]
        indexedQueries.sort(key=lambda item: item[0])

        ans = [0] * len(queries)
        serverCounts = {}
        left = 0
        right = 0

        for queryTime, queryIndex in indexedQueries:
            # Expand the window to the right, adding logs within the current query's time.
            while right < len(logs) and logs[right][1] <= queryTime:
                serverId = logs[right][0]
                serverCounts[serverId] = serverCounts.get(serverId, 0) + 1
                right += 1

            # Shrink the window from the left, removing logs that are now outside the window.
            windowStart = queryTime - x
            while left < right and logs[left][1] < windowStart:
                serverId = logs[left][0]
                serverCounts[serverId] -= 1
                if serverCounts[serverId] == 0:
                    del serverCounts[serverId]
                left += 1

            # Calculate the number of inactive servers and store it.
            activeCount = len(serverCounts)
            ans[queryIndex] = n - activeCount

        return ans