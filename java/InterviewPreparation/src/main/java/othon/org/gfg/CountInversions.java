package othon.org.gfg;

import lombok.extern.slf4j.Slf4j;
import lombok.var;

import java.util.Arrays;

/**
 * Link:https://www.geeksforgeeks.org/counting-inversions/
 * <pre>
 * Input: arr[] = {8, 4, 2, 1}
 * Output: 6
 *
 * Explanation: Given array has six inversions:
 * (8,4), (4,2),(8,2), (8,1), (4,1), (2,1).
 *
 *
 * Input: arr[] = {3, 1, 2}
 * Output: 2
 *
 * Explanation: Given array has two inversions:
 * (3, 1), (3, 2)
 * </pre>
 */

@Slf4j
public class CountInversions {
    public static void main(String[] args) {
        Solution s = new Solution();
        int[] arr = { 1, 20, 6, 4, 5 };
        log.info("Inversions {} ", s.mergeSortEnhanced(arr, 0, arr.length - 1));

    }

    static class Solution {

        public int mergeSortEnhanced(int[] arr, int l, int r) {
            int count = 0;
            if (l< r) {
                int m = (l+r) / 2;
                count += mergeSortEnhanced(arr,l, m);
                count += mergeSortEnhanced(arr, m + 1, r);
                count += mergeAndCount(arr,l,m,r);
            }
            return count;
        }

        private int mergeAndCount(int[] arr, int l, int m, int r) {
            int[] left = Arrays.copyOfRange(arr, l , m + 1);
            int[] right = Arrays.copyOfRange(arr, m + 1, r + 1);
            int i =0 , j = 0, current = l;
            int swaps = 0;
            while (i <left.length && j<right.length) {
                if (left[i] <= right[j]) {
                    arr[current++]  = left[i++];
                } else {
                    arr[current++]  = right[j++];
                    swaps += (m + 1) - (l + i);
                }
            }
            // copy the remaining numbers of left
            while ( i < left.length) arr[current++] = left[i++];
            // copy the remaining numbers of left
            while (j < right.length) arr[current++] = right[j++];
            log.info("swaps{} - {}", swaps, arr);
            return swaps;
        }
    }
}
