// Leetcode 3318: Find X-Sum of All K-Long Subarrays I
// https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/
// Solved on 4th of November, 2025
import java.util.HashMap;
import java.util.TreeSet;

class Solution {
    private static class Node {
        int value;
        int count;

        Node(int v, int c) {
            value = v;
            count = c;
        }
    }

    /**
     * Calculates the "X-Sum" for all K-long subarrays in the given array.
     * @param nums The input array of integers.
     * @param k The length of the subarrays.
     * @param x The number of most frequent elements to consider for the sum.
     * @return An array containing the X-Sum for each K-long subarray.
     */
    public int[] findXSum(int[] nums, int k, int x) {
        int n = nums.length;
        int outLen = n - k + 1;
        int[] answer = new int[outLen];

        HashMap<Integer, Integer> freqMap = new HashMap<>();
        TreeSet<Node> tree = new TreeSet<>((a, b) -> {
            int c = Integer.compare(b.count, a.count);
            if (c != 0) return c;
            return Integer.compare(b.value, a.value);
        });

        for (int i = 0; i < k; ++i) {
            int v = nums[i];
            int old = freqMap.getOrDefault(v, 0);
            if (old > 0) tree.remove(new Node(v, old));
            int neo = old + 1;
            freqMap.put(v, neo);
            tree.add(new Node(v, neo));
        }

        int idx = 0;
        while (true) {
            long sum = 0;
            int taken = 0;
            for (Node node : tree) {
                sum += (long) node.value * node.count;
                taken++;
                if (taken == x) break;
            }
            answer[idx++] = (int) sum;

            if (idx == outLen) break;

            int outVal = nums[idx - 1];
            int inVal = nums[idx + k - 1];

            int oldOut = freqMap.get(outVal);
            tree.remove(new Node(outVal, oldOut));
            if (oldOut == 1) {
                freqMap.remove(outVal);
            } else {
                freqMap.put(outVal, oldOut - 1);
                tree.add(new Node(outVal, oldOut - 1));
            }

            int oldIn = freqMap.getOrDefault(inVal, 0);
            if (oldIn > 0) tree.remove(new Node(inVal, oldIn));
            freqMap.put(inVal, oldIn + 1);
            tree.add(new Node(inVal, oldIn + 1));
        }

        return answer;
    }
}