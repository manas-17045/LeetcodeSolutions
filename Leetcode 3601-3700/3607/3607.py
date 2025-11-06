# Leetcode 3607: Power Grid Maintenance
# https://leetcode.com/problems/power-grid-maintenance/
# Solved on 6th of November, 2025
import heapq


class Solution:
    def processQueries(self, c: int, connections: list[list[int]], queries: list[list[int]]) -> list[int]:
        """
        Processes a series of queries related to a power grid, including finding the
        lowest-ID operational station in a connected component and taking stations offline.

        Args:
            c (int): The total number of stations, from 1 to c.
            connections (list[list[int]]): A list of connections, where each connection
                                           [u, v] indicates a direct link between station u and station v.
            queries (list[list[int]]): A list of queries. Each query is either:
                                       - [1, station_id]: Find the lowest-ID operational station in the component of station_id.
                                       - [2, station_id]: Take station_id offline.
        Returns:
            list[int]: A list of results for each query of type 1.
                       - If the queried station itself is operational, return its ID.
                       - If not, return the lowest-ID operational station in its component.
                       - If no operational station is found in the component, return -1.
        """
        parent = list(range(c + 1))
        size = [1] * (c + 1)
        gridHeaps = {i: [i] for i in range(1, c + 1)}
        operationalStatus = [True] * (c + 1)

        def findStation(i: int) -> int:
            if parent[i] == i:
                return i
            parent[i] = findStation(parent[i])
            return parent[i]

        def unionStations(u: int, v: int):
            rootU = findStation(u)
            rootV = findStation(v)

            if rootU == rootV:
                return

            if size[rootU] > size[rootV]:
                rootU, rootV = rootV, rootU

            parent[rootU] = rootV
            size[rootV] += size[rootU]

            heapU = gridHeaps.pop(rootU)
            heapV = gridHeaps[rootV]

            for stationId in heapU:
                heapq.heappush(heapV, stationId)

        for u, v in connections:
            unionStations(u, v)

        results = []

        for query in queries:
            queryType = query[0]
            station = query[1]

            if queryType == 1:
                if operationalStatus[station]:
                    results.append(station)
                else:
                    root = findStation(station)
                    heap = gridHeaps.get(root)

                    if not heap:
                        results.append(-1)
                        continue

                    while heap and not operationalStatus[heap[0]]:
                        heapq.heappop(heap)

                    if heap:
                        results.append(heap[0])
                    else:
                        results.append(-1)

            elif queryType == 2:
                operationalStatus[station] = False

        return results