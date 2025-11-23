// Leetcode 3072: Distribute Elements Into Two Arrays II
// https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/
// Solved on 23rd of November, 2025
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    /**
     * Distributes elements from the input array `nums` into two arrays, `list1` and `list2`,
     * based on a specific rule involving greater element counts and array sizes.
     * @param nums The input array of integers.
     * @return An array containing the elements of `list1` followed by the elements of `list2`.
     */
    public int[] resultArray(int[] nums) {
        int[] sortedNums = nums.clone();
        Arrays.sort(sortedNums);
        int n = sortedNums.length;
        int uniqueCount = 0;
        for (int i = 0; i < n; i++) {
            if (i == 0 || sortedNums[i] != sortedNums[i - 1]) {
                sortedNums[uniqueCount++] = sortedNums[i];
            }
        }

        List<Integer> list1 = new ArrayList<>();
        List<Integer> list2 = new ArrayList<>();
        int[] tree1 = new int[uniqueCount + 2];
        int[] tree2 = new int[uniqueCount + 2];

        list1.add(nums[0]);
        update(tree1, getRank(sortedNums, uniqueCount, nums[0]), 1);

        list2.add(nums[1]);
        update(tree2, getRank(sortedNums, uniqueCount, nums[1]), 1);

        for (int i = 2; i < n; i++) {
            int val = nums[i];
            int rank = getRank(sortedNums, uniqueCount, val);
            int greaterCount1 = list1.size() - query(tree1, rank);
            int greaterCount2 = list2.size() - query(tree2, rank);

            if (greaterCount1 > greaterCount2) {
                list1.add(val);
                update(tree1, rank, 1);
            } else if (greaterCount1 < greaterCount2) {
                list2.add(val);
                update(tree2, rank, 1);
            } else {
                if (list1.size() <= list2.size()) {
                    list1.add(val);
                    update(tree1, rank, 1);
                } else {
                    list2.add(val);
                    update(tree2, rank, 1);
                }
            }
        }

        int[] result = new int[n];
        int index = 0;
        for (int val : list1) {
            result[index++] = val;
        }
        for (int val : list2) {
            result[index++] = val;
        }
        return result;
    }

    private int getRank(int[] sortedNums, int length, int val) {
        int left = 0;
        int right = length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (sortedNums[mid] == val) {
                return mid + 1;
            } else if (sortedNums[mid] < val) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }

    private void update(int[] tree, int index, int val) {
        while (index < tree.length) {
            tree[index] += val;
            index += index & (-index);
        }
    }

    private int query(int[] tree, int index) {
        int sum = 0;
        while (index > 0) {
            sum += tree[index];
            index -= index & (-index);
        }
        return sum;
    }
}