// Leetcode 1943: Describe the Painting
// https://leetcode.com/problems/describe-the-painting/
// Solved on 5th of November, 2025
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.TreeMap;

class Solution {
    /**
     * Given a list of segments where each segment is defined as [start, end, color],
     * this function describes the painting by splitting it into minimal segments where each segment has a uniform color.
     * @param segments An array of integer arrays, where each inner array represents a segment [start, end, color].
     * @return A list of lists of Longs, where each inner list represents a described segment [start, end, total_color].
     */
    public List<List<Long>> splitPainting(int[][] segments) {
        TreeMap<Integer, Long> events = new TreeMap<>();
        for (int[] seg : segments) {
            int start = seg[0];
            int end = seg[1];
            long color = seg[2];
            events.put(start, events.getOrDefault(start, 0L) + color);
            events.put(end, events.getOrDefault(end, 0L) - color);
        }
        List<List<Long>> result = new ArrayList<>();
        long curr = 0L;
        int prev = -1;
        for (Map.Entry<Integer, Long> e : events.entrySet()) {
            int pos = e.getKey();
            if (prev != -1 && prev < pos && curr > 0) {
                List<Long> part = new ArrayList<>();
                part.add((long)prev);
                part.add((long)pos);
                part.add(curr);
                result.add(part);
            }
            curr += e.getValue();
            prev = pos;
        }
        return result;
    }
}