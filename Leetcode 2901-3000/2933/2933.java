// Leetcode 2933: High-Access Employees
// https://leetcode.com/problems/high-access-employees/
// Solved on 5th of November, 2025
import java.util.*;

class Solution {
    /**
     * Finds employees who have "high access", defined as accessing the system 3 or more times within a 1-hour period.
     *
     * @param access_times A list of lists, where each inner list contains an employee's name and their access time (e.g., ["john", "0500"]).
     * @return A list of names of employees who have high access.
     */
    public List<String> findHighAccessEmployees(List<List<String>> access_times) {
        Map<String, List<Integer>> map = new HashMap<>();
        for (List<String> pair : access_times) {
            String name = pair.get(0);
            String time = pair.get(1);
            int minutes = Integer.parseInt(time.substring(0, 2)) * 60 + Integer.parseInt(time.substring(2));
            map.computeIfAbsent(name, k -> new ArrayList<>()).add(minutes);
        }
        List<String> result = new ArrayList<>();
        for (Map.Entry<String, List<Integer>> entry : map.entrySet()) {
            List<Integer> times = entry.getValue();
            Collections.sort(times);
            int left = 0;
            for (int right = 0; right < times.size(); right++) {
                while (times.get(right) - times.get(left) > 59) left++;
                if (right - left + 1 >= 3) {
                    result.add(entry.getKey());
                    break;
                }
            }
        }
        return result;
    }
}
