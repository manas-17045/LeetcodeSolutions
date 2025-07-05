# Leetcode 1606: Find Servers That Handled Most Number of Requests
# https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/
# Solved on 5th of July, 2025
import heapq


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        """
        Finds the servers that handled the most number of requests.

        Args:
            k (int): The number of servers.
            arrival (list[int]): A list where arrival[i] is the arrival time of the i-th request.
            load (list[int]): A list where load[i] is the time duration the i-th request takes.

        Returns:
            list[int]: A list of server IDs (0-indexed) that handled the maximum number of requests.
                       If no requests are handled, returns all server IDs.

        The solution uses two min-heaps to manage available servers:
        - `availableHigh`: Stores server IDs >= the current target server ID (i % k).
        - `availableLow`: Stores server IDs < the current target server ID (i % k).
        A third min-heap `busyServers` stores (finish_time, server_id) for busy servers.
        Requests are assigned to the first available server starting from `i % k` in a
        round-robin manner.
        """
        requestsHandled = [0] * k
        busyServers = []

        availableHigh = list(range(k))
        heapq.heapify(availableHigh)
        availableLow = []

        for i in range(len(arrival)):
            currentTime = arrival[i]
            currentLoad = load[i]
            target = i % k

            while busyServers and busyServers[0][0] <= currentTime:
                finishTime, serverId = heapq.heappop(busyServers)
                if serverId < target:
                    heapq.heappush(availableLow, serverId)
                else:
                    heapq.heappush(availableHigh, serverId)

            # Transfer servers that are now less than the new target from the high heap to the low heap
            while availableHigh and availableHigh[0] < target:
                serverId = heapq.heappop(availableHigh)
                heapq.heappush(availableLow, serverId)

            # Transfer servers that are now greater than or equal to the new target
            # from the low heap to the high heap. This is needed for correctness
            # when the target index wraps around.
            tempRelocate = []
            while availableLow and availableLow[0] >= target:
                tempRelocate.append(heapq.heappop(availableLow))
            for sId in tempRelocate:
                heapq.heappush(availableHigh, sId)

            serverToUse = -1
            if availableHigh:
                serverToUse = heapq.heappop(availableHigh)
            elif availableLow:
                serverToUse = heapq.heappop(availableLow)

            if serverToUse != -1:
                requestsHandled[serverToUse] += 1
                heapq.heappush(busyServers, (currentTime + currentLoad, serverToUse))

        maxRequests = 0
        if any(requestsHandled):
            maxRequests = max(requestsHandled)
        else:
            return list(range(k))

        busiest = []
        for i, count in enumerate(requestsHandled):
            if count == maxRequests:
                busiest.append(i)

        return busiest