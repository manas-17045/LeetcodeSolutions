// Leetcode 4012: Count of Unfinished Tasks After Each Shift
// https://leetcode.com/problems/count-of-unfinished-tasks-after-each-shift/
// Solved on 4th of September, 2026
class Solution {
    /**
     * Calculates the number of unfinished tasks remaining after each shift by tracking
     * cumulative progress and using binary search over the prefix sums of task durations.
     *
     * @param tasks an array where each element represents the time required to complete that task
     * @param shifts an array where each element represents the duration of that shift
     * @return an array containing the count of unfinished tasks immediately after each shift
     */
    public int[] countTasks(int[] tasks, int[] shifts) {
        int taskCount = tasks.length;
        int shiftCount = shifts.length;
        long[] prefixSums = new long[taskCount];
        prefixSums[0] = tasks[0];
        for (int i = 1; i < taskCount; i++) {
            prefixSums[i] = prefixSums[i - 1] + tasks[i];
        }

        long totalTime = prefixSums[taskCount - 1];
        long currentWork = 0;
        int[] result = new int[shiftCount];

        for (int j = 0; j < shiftCount; j++) {
            currentWork += shifts[j];
            if (currentWork >= totalTime) {
                result[j] = 0;
                currentWork = 0;
            } else {
                int low = 0;
                int high = taskCount - 1;
                int completedTasks = 0;
                while (low <= high) {
                    int mid = low + (high - low) / 2;
                    if (prefixSums[mid] <= currentWork) {
                        completedTasks = mid + 1;
                        low = mid + 1;
                    } else {
                        high = mid - 1;
                    }
                }
                result[j] = taskCount - completedTasks;
            }
        }

        return result;
    }
}