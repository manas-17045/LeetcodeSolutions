// Leetcode 3488: Closest Equal Element Queries
// https://leetcode.com/problems/closest-equal-element-queries/
// Solved on 16th of April, 2026
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    /**
     * Solves queries to find the minimum distance to the closest equal element in a circular array.
     *
     * @param nums    An array of integers.
     * @param queries An array of indices representing the target elements in nums.
     * @return A list of integers where each element is the minimum distance to another occurrence of the same value.
     */
    public List<Integer> solveQueries(int[] nums, int[] queries) {
        int n = nums.length;
        Map<Integer, List<Integer>> valueIndices = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            valueIndices.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }
        
        List<Integer> answer = new ArrayList<>(queries.length);
        
        for (int queryIndex : queries) {
            int targetValue = nums[queryIndex];
            List<Integer> indicesList = valueIndices.get(targetValue);
            
            if (indicesList.size() == 1) {
                answer.add(-1);
                continue;
            }
            
            int left = 0;
            int right = indicesList.size() - 1;
            int targetPos = -1;
            
            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (indicesList.get(mid) == queryIndex) {
                    targetPos = mid;
                    break;
                } else if (indicesList.get(mid) < queryIndex) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
            
            int prevIndex = targetPos > 0 ? targetPos - 1 : indicesList.size() - 1;
            int nextIndex = targetPos < indicesList.size() - 1 ? targetPos + 1 : 0;
            
            int prevDiff = Math.abs(queryIndex - indicesList.get(prevIndex));
            int prevDist = Math.min(prevDiff, n - prevDiff);
            
            int nextDiff = Math.abs(queryIndex - indicesList.get(nextIndex));
            int nextDist = Math.min(nextDiff, n - nextDiff);
            
            answer.add(Math.min(prevDist, nextDist));
        }
        
        return answer;
    }
}