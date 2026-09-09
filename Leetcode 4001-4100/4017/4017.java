// Leetcode 4017: Peaks in Array II
// https://leetcode.com/problems/peaks-in-array-ii/
// Solved on 9th of September, 2026
import java.util.ArrayList;
import java.util.List;
import java.util.TreeSet;

class Solution {
    /**
     * Calculates the number of peak subarrays for a series of queries and applies element updates to the array.
     * A peak subarray is defined as a contiguous subarray of length at least 3 containing at least one element 
     * strictly greater than its adjacent elements within the subarray.
     *
     * @param nums    the initial array of integers
     * @param queries the 2D array of queries where each query is either a type 1 (count peak subarrays) 
     *                or type 2 (update an element)
     * @return an array of long integers representing the answers to all type 1 queries in order
     */
    public long[] countOfPeaks(int[] nums, int[][] queries) {
        int arrayLength = nums.length;
        TreeSet<Integer> peaks = new TreeSet<>();
        long[] bit = new long[arrayLength + 1];
        List<Long> resultList = new ArrayList<>();
        
        for (int i = 1; i < arrayLength - 1; i++) {
            if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) {
                addPeak(i, peaks, bit);
            }
        }
        
        for (int[] query : queries) {
            if (query[0] == 1) {
                int leftBound = query[1];
                int rightBound = query[2];
                Integer firstPeak = peaks.higher(leftBound);
                
                if (firstPeak == null || firstPeak >= rightBound) {
                    resultList.add(0L);
                } else {
                    Integer lastPeak = peaks.lower(rightBound);
                    Integer previousPeakObj = peaks.lower(firstPeak);
                    int previousPeak = (previousPeakObj == null) ? 0 : previousPeakObj;
                    long prefixSum = queryBit(bit, lastPeak) - queryBit(bit, firstPeak - 1);
                    long resultValue = (long) rightBound * (lastPeak - leftBound) - prefixSum + (long) firstPeak * (leftBound - previousPeak);
                    resultList.add(resultValue);
                }
            } else {
                int updateIndex = query[1];
                int updateValue = query[2];
                boolean[] oldStatus = new boolean[3];
                
                for (int j = 0; j < 3; j++) {
                    int currentPeakIndex = updateIndex - 1 + j;
                    if (currentPeakIndex > 0 && currentPeakIndex < arrayLength - 1) {
                        oldStatus[j] = (nums[currentPeakIndex] > nums[currentPeakIndex - 1] && nums[currentPeakIndex] > nums[currentPeakIndex + 1]);
                    }
                }
                
                nums[updateIndex] = updateValue;
                
                for (int j = 0; j < 3; j++) {
                    int currentPeakIndex = updateIndex - 1 + j;
                    if (currentPeakIndex > 0 && currentPeakIndex < arrayLength - 1) {
                        boolean newStatus = (nums[currentPeakIndex] > nums[currentPeakIndex - 1] && nums[currentPeakIndex] > nums[currentPeakIndex + 1]);
                        if (oldStatus[j] && !newStatus) {
                            removePeak(currentPeakIndex, peaks, bit);
                        } else if (!oldStatus[j] && newStatus) {
                            addPeak(currentPeakIndex, peaks, bit);
                        }
                    }
                }
            }
        }
        
        long[] finalResult = new long[resultList.size()];
        for (int i = 0; i < resultList.size(); i++) {
            finalResult[i] = resultList.get(i);
        }
        return finalResult;
    }

    private void addPeak(int peakIndex, TreeSet<Integer> peaks, long[] bit) {
        Integer previousPeakObj = peaks.lower(peakIndex);
        int previousPeak = (previousPeakObj == null) ? 0 : previousPeakObj;
        Integer nextPeak = peaks.higher(peakIndex);
        long peakValue = (long) peakIndex * (peakIndex - previousPeak);
        
        addBit(bit, peakIndex, peakValue);
        
        if (nextPeak != null) {
            long oldNextValue = (long) nextPeak * (nextPeak - previousPeak);
            addBit(bit, nextPeak, -oldNextValue);
            long newNextValue = (long) nextPeak * (nextPeak - peakIndex);
            addBit(bit, nextPeak, newNextValue);
        }
        
        peaks.add(peakIndex);
    }

    private void removePeak(int peakIndex, TreeSet<Integer> peaks, long[] bit) {
        peaks.remove(peakIndex);
        Integer previousPeakObj = peaks.lower(peakIndex);
        int previousPeak = (previousPeakObj == null) ? 0 : previousPeakObj;
        Integer nextPeak = peaks.higher(peakIndex);
        long peakValue = (long) peakIndex * (peakIndex - previousPeak);
        
        addBit(bit, peakIndex, -peakValue);
        
        if (nextPeak != null) {
            long oldNextValue = (long) nextPeak * (nextPeak - peakIndex);
            addBit(bit, nextPeak, -oldNextValue);
            long newNextValue = (long) nextPeak * (nextPeak - previousPeak);
            addBit(bit, nextPeak, newNextValue);
        }
    }

    private void addBit(long[] bit, int index, long value) {
        for (; index < bit.length; index += index & -index) {
            bit[index] += value;
        }
    }

    private long queryBit(long[] bit, int index) {
        long sum = 0;
        for (; index > 0; index -= index & -index) {
            sum += bit[index];
        }
        return sum;
    }
}