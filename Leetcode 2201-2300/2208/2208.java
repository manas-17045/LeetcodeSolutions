// Leetcode 2208: Minimum Operations to Halve Array Sum
// https://leetcode.com/problems/minimum-operations-to-halve-array-sum/
// Solved on 30th of November, 2025
import java.util.Collections;
import java.util.PriorityQueue;

class Solution {
    /**
     * Calculates the minimum number of operations required to halve the total sum of an array.
     * In each operation, you can choose any number in the array and replace it with half of its value.
     * @param nums An array of integers.
     * @return The minimum number of operations to reduce the array's sum by at least half.
     */
    public int halveArray(int[] nums) {
        PriorityQueue<Double> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        double currentSum = 0;
        
        for (int num : nums) {
            currentSum += num;
            maxHeap.add((double) num);
        }
        
        double targetSum = currentSum / 2.0;
        int operationCount = 0;
        
        while (currentSum > targetSum) {
            double maxValue = maxHeap.poll();
            double halvedValue = maxValue / 2.0;
            
            currentSum -= halvedValue;
            maxHeap.add(halvedValue);
            
            operationCount++;
        }
        
        return operationCount;
    }
}