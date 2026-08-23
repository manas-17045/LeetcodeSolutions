# Leetcode 4001: Aggregate Two Time Series
# https://leetcode.com/problems/aggregate-two-time-series/
# Solved on 23rd of August, 2026
class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        """
        Aggregates two time series by merging them at common timestamps and taking the 
        latest value for each time series at unique timestamps.
        @param series1 First time series as a 2D array of [timestamp, value].
        @param series2 Second time series as a 2D array of [timestamp, value].
        @return The aggregated time series as a 2D array of [timestamp, value].
        """
        iOne = len(series1) - 1
        iTwo = len(series2) - 1
        vOne = 0
        vTwo = 0
        aSeries = []

        while iOne >= 0 or iTwo >= 0:
            if iOne >= 0 and iTwo >= 0:
                timeOne = series1[iOne][0]
                timeTwo = series2[iTwo][0]

                if timeOne > timeTwo:
                    currentTime = timeOne
                    vOne = series1[iOne][1]
                    iOne -= 1
                elif timeTwo > timeOne:
                    currentTime = timeTwo
                    vTwo = series2[iTwo][1]
                    iTwo -= 1
                else:
                    currentTime = timeOne
                    vOne = series1[iOne][1]
                    vTwo = series2[iTwo][1]
                    iOne -= 1
                    iTwo -= 1
            elif iOne >= 0:
                currentTime = series1[iOne][0]
                vOne = series1[iOne][1]
                iOne -= 1
            else:
                currentTime = series2[iTwo][0]
                vTwo = series2[iTwo][1]
                iTwo -= 1

            aSeries.append([currentTime, vOne + vTwo])

        aSeries.reverse()
        return aSeries