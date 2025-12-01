// Leetcode 2808: Minimum Seconds to Equalize a Circular Array
// https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/
// Solved on 1st of December, 2025
class Solution {
    /**
     * Calculates the minimum seconds required to equalize a circular array.
     *
     * @param nums The input list of integers representing the circular array.
     * @return The minimum number of seconds to make all elements in the array equal.
     */
    public int minimumSeconds(List<Integer> nums) {
        int n = nums.size();
        Map<Integer, List<Integer>> indexMap = new HashMap<>();

        for (int i = 0; i < n; i++) {
            indexMap.computeIfAbsent(nums.get(i), k -> new ArrayList<>()).add(i);
        }

        int minSeconds = n;

        for (List<Integer> indices : indexMap.values()) {
            indices.add(indices.get(0) + n);
            int maxGap = 0;
            for (int i = 0; i < indices.size() - 1; i++) {
                maxGap = Math.max(maxGap, indices.get(i + 1) - indices.get(i));
            }
            minSeconds = Math.min(minSeconds, maxGap / 2);
        }

        return minSeconds;
    }
}