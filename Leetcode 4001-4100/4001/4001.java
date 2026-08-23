// Leetcode 4001: Aggregate Two Time Series
// https://leetcode.com/problems/aggregate-two-time-series/ 
// Solved on 23rd of August, 2026
class Solution {
    /**
     * Aggregates two time series by merging them at common timestamps and taking the 
     * latest value for each time series at unique timestamps.
     * @param series1 First time series as a 2D array of [timestamp, value].
     * @param series2 Second time series as a 2D array of [timestamp, value].
     * @return The aggregated time series as a 2D array of [timestamp, value].
     */
    public List<List<Integer>> aggregateTimeSeries(int[][] series1, int[][] series2) {
        List<List<Integer>> result = new ArrayList<>();
        int index1 = series1.length - 1;
        int index2 = series2.length - 1;
        int latestVal1 = 0;
        int latestVal2 = 0;

        while (index1 >= 0 || index2 >= 0) {
            int currentTimestamp;
            if (index1 >= 0 && index2 >= 0) {
                if (series1[index1][0] > series2[index2][0]) {
                    currentTimestamp = series1[index1][0];
                    latestVal1 = series1[index1][1];
                    index1--;
                } else if (series1[index1][0] < series2[index2][0]) {
                    currentTimestamp = series2[index2][0];
                    latestVal2 = series2[index2][1];
                    index2--;
                } else {
                    currentTimestamp = series1[index1][0];
                    latestVal1 = series1[index1][1];
                    latestVal2 = series2[index2][1];
                    index1--;
                    index2--;
                }
            } else if (index1 >= 0) {
                currentTimestamp = series1[index1][0];
                latestVal1 = series1[index1][1];
                index1--;
            } else {
                currentTimestamp = series2[index2][0];
                latestVal2 = series2[index2][1];
                index2--;
            }

            result.add(Arrays.asList(currentTimestamp, latestVal1 + latestVal2));
        }

        Collections.reverse(result);
        return result;
    }
}