# Leetcode 2747: Count Zero Request Servers
# https://leetcode.com/problems/count-zero-request-servers/
# Solved on 10th of August, 2025
class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        """
        Calculates the number of servers that have zero requests within a specific time window for each query.

        Args:
            n (int): The total number of servers.
            logs (list[list[int]]): A list of log entries, where each entry is [server_id, time].
            x (int): The duration of the time window.
            queries (list[int]): A list of query times.
        Returns:
            list[int]: A list of integers, where each element is the count of servers with zero requests
                        for the corresponding query time.
        """
        # Sort logs by time (each log: [server_id, time])
        logs.sort(key=lambda l: l[1])

        # Keep queries with original indices and sort by query time
        indexed_queries = sorted([(q, i) for i, q in enumerate(queries)])

        cnt = [0] * (n + 1)  # cnt[server_id] = number of logs for that server in current window
        res = [0] * len(queries)

        l = 0  # left pointer into logs (first log that is within current window)
        r = 0  # right pointer into logs (one past last included log)
        unique = 0  # number of servers that have at least one request in current window

        L = len(logs)
        for qtime, qidx in indexed_queries:
            # Include logs with time <= qtime
            while r < L and logs[r][1] <= qtime:
                sid = logs[r][0]
                if cnt[sid] == 0:
                    unique += 1
                cnt[sid] += 1
                r += 1

            # Exclude logs with time < qtime - x  (window is [qtime - x, qtime], inclusive)
            window_start = qtime - x
            while l < L and logs[l][1] < window_start:
                sid = logs[l][0]
                cnt[sid] -= 1
                if cnt[sid] == 0:
                    unique -= 1
                l += 1

            # Servers with zero requests = total servers - servers with at least one request
            res[qidx] = n - unique

        return res