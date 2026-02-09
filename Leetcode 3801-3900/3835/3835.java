// Leetcode 3835: Count Subarrays With Cost Less Than or Equal to K
// https://leetcode.com/problems/count-subarrays-with-cost-less-than-or-equal-to-k/
// Solved on 9th of February, 2026
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    /**
     * Counts the number of subarrays where the cost (max - min) * length is less than or equal to k.
     * @param nums The input array of integers.
     * @param k The maximum allowable cost for a subarray.
     * @return The total count of subarrays satisfying the condition.
     */
    public long countSubarrays(int[] nums, long k) {
        long count = 0;
        int left = 0;
        Deque<Integer> maxDeque = new ArrayDeque<>();
        Deque<Integer> minDeque = new ArrayDeque<>();

        for (int right = 0; right < nums.length; right++) {
            while (!maxDeque.isEmpty() && nums[maxDeque.peekLast()] <= nums[right]) {
                maxDeque.pollLast();
            }
            maxDeque.addLast(right);

            while (!minDeque.isEmpty() && nums[minDeque.peekLast()] >= nums[right]) {
                minDeque.pollLast();
            }
            minDeque.addLast(right);

            while (true) {
                long diff = nums[maxDeque.peekFirst()] - nums[minDeque.peekFirst()];
                long cost = diff * (right - left + 1);

                if (cost <= k) {
                    break;
                }

                if (maxDeque.peekFirst() == left) {
                    maxDeque.pollFirst();
                }
                if (minDeque.peekFirst() == left) {
                    minDeque.pollFirst();
                }
                left++;
            }
            count += (right - left + 1);
        }
        return count;
    }
}