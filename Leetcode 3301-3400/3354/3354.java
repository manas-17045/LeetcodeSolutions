// Leetcode 3354: Make Array Elements Equal to Zero
// https://leetcode.com/problems/make-array-elements-equal-to-zero/
// Solved on 28th of October, 2025
import java.util.ArrayList;
import java.util.List;

class Solution {
    /**
     * Counts the number of valid selections to make all array elements zero.
     * A selection is valid if, starting from an element with value 0,
     * and moving left or right, all elements can be decremented to zero.
     * @param nums The input array of integers.
     * @return The number of valid selections.
     */
    public int countValidSelections(int[] nums) {
        int n = nums.length;
        int validCount = 0;
        List<Integer> startIndices = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                startIndices.add(i);
            }
        }

        int[] initialDirections = {1, -1};

        for (int startIndex : startIndices) {
            for (int startDir : initialDirections) {
                
                int[] tempNums = nums.clone();
                int curr = startIndex;
                int dir = startDir;

                while (curr >= 0 && curr < n) {
                    if (tempNums[curr] > 0) {
                        tempNums[curr]--;
                        dir = -dir;
                    }
                    curr = curr + dir;
                }

                if (this.isAllZero(tempNums)) {
                    validCount++;
                }
            }
        }
        return validCount;
    }

    private boolean isAllZero(int[] arr) {
        for (int val : arr) {
            if (val != 0) {
                return false;
            }
        }
        return true;
    }
}