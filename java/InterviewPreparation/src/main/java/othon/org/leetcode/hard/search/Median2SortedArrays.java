package othon.org.leetcode.hard.search;

import lombok.extern.slf4j.Slf4j;
import lombok.var;
import othon.org.leetcode.utils.Deserializer;

/**
 * Link: https://leetcode.com/problems/median-of-two-sorted-arrays/solution/
 *  Explanation: https://www.youtube.com/watch?v=LPFhl65R7ww&feature=emb_logo
 * <p>
 * TODO:
 */

@Slf4j
public class Median2SortedArrays {
    public static void main(String[] args) {
        Solution s = new Solution();
        var A = Deserializer.toIntArray("[1, 3]");
        var B = Deserializer.toIntArray("[2, 4]");
        s.findMedianSortedArrays(A, B);
    }

    static class Solution {
        public double findMedianSortedArrays(int[] shortesArray, int[] largestArray) {
            int m = shortesArray.length;
            int n = largestArray.length;
            // we want to do a binary search on the smallest array so swap the array if it first one is larger thatn the other
            if (m> n) {
                int temp = n; n = m; m=temp;
                int[] tempArr = largestArray; largestArray=shortesArray; shortesArray=tempArr;
            }
            /*
             * The idea is to find the middle position. If the total elements is odd then return the
             * max(A[i], B[j]) where the i and j are the position in the array that point to the half of
             * the elements. If total element is even then we need avg(min(A[i+1], B[[j+1),max(A[i], B[j]))
             * shortest = x0,x1,|x2 x3,x4,x5
             *
             * longest = y0,y1,y2,y3, y4 | y5,y6,y7
             *
             * We are looking for: x1 < y5 && y3<x3
             * If x1 > y5 Then move to the left
             * If y4 > x2 Move to the right
             */
            // we do a binary search on the smallest array to find the middle element
            // for the other array, the position is half - i
            int left = 0; int right = m; int halfOfAllElements = (m + n) / 2;
            double median = 0.0d;
            while (left<= right) {
                int middle = (right + left) / 2;
                int j = halfOfAllElements - middle; // this creates the pointer to the other array

                if (middle < right
                        && shortesArray[middle]<largestArray[j-1]) { // we are looking the position where
                    left = middle + 1;
                } else if (middle > left
                    && shortesArray[middle -1]>largestArray[j]) { // we are looking the position where
                    right = middle -1;
                } else   {
                    int maxLeftHalf = 0;
                    /*
                     * In the next 2 ifs we compare if the pointers of the arrays are  at zero. Since middle is a pointer
                     * that belongs to shortestArray. If shortestArray[middle] points to the first element on the right
                     * half of the numbers on the shortestArray. If it middle == 0 then we can't pick middle -1 to grab
                     * the last element of the left half then we have to pick it from the other array, the largestArray.
                     */
                    if (middle ==0) maxLeftHalf = largestArray[j-1];
                    if (j ==0) maxLeftHalf = shortesArray[middle-1];
                    else maxLeftHalf = Math.max(largestArray[j-1], shortesArray[middle-1]);
                    if (n+m%2 == 1) return maxLeftHalf;

                    //get the other number
                    int minRightHalf = 0;
                    if (middle == m) minRightHalf = largestArray[j];
                    if (j == n) minRightHalf = shortesArray[middle];
                    else minRightHalf = Math.min(largestArray[j], shortesArray[middle]);
                    return (double)(maxLeftHalf + minRightHalf) / 2;
                }
            }
            return median;
        }
    }
}
