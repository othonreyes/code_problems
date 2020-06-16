package othon.org.leetcode.medium.sort;

import lombok.extern.slf4j.Slf4j;
import lombok.var;
import othon.org.leetcode.utils.Deserializer;

import java.util.Arrays;

/**
 * Link:
 * <p>
 * TODO:    https://leetcode.com/problems/k-closest-points-to-origin
 */

@Slf4j
public class KClosestPointstoOrigin {
    public static void main(String[] args) {
        Solution s = new Solution();
        var input = Deserializer.toIntMatrix("[[6,10],[-3,3],[-2,5],[0,2]]");
        log.info("{}", s.kClosest(input, 3));
    }

    static class Solution {
        public int[][] kClosest(int[][] points, int K) {
            mergeSort(points, 0, points.length-1);
            return Arrays.copyOfRange(points, 0, K);
        }

        void mergeSort(int[][] points, int left, int right) {
            if (left< right) {
                int middle = (left + right) / 2;
                mergeSort(points, left, middle);
                mergeSort(points, middle + 1, right);
                merge(points, left, middle, right);
            }
        }

        void merge(int[][] points, int left, int middle, int right) {
            int[][] leftArr = Arrays.copyOfRange(points, left, middle + 1);
            int[][] rightArr = Arrays.copyOfRange(points, middle + 1, right + 1);
            int l=0, r=0, curr = l;

            while(l<leftArr.length && r<rightArr.length) {
                if (lte(leftArr[l], rightArr[r])) { // left smaller or equals
                    points[curr++] = leftArr[l++];
                } else {
                    points[curr++] = rightArr[r++];
                }
            }
            //copy remaining
            while(l<leftArr.length) {
                points[curr++] = leftArr[l++];
            }
            while(r<rightArr.length) {
                points[curr++] = rightArr[r++];
            }
        }

        boolean lte(int[] left, int[] right) {
            int edl = (int)Math.pow(left[0], 2) + (int)Math.pow(left[1], 2);
            int edr = (int)Math.pow(right[0], 2) + (int)Math.pow(right[1], 2);
            return edl <= edr;
        }
    }
}
