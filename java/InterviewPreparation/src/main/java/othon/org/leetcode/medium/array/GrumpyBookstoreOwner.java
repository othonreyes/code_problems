package othon.org.leetcode.medium.array;

import lombok.extern.slf4j.Slf4j;
import lombok.var;
import othon.org.leetcode.utils.Deserializer;

/**
 * Link:
 * <p>
 * TODO:
 */

@Slf4j
public class GrumpyBookstoreOwner {
    public static void main(String[] args) {
        Solution s = new Solution();

        var input = 3;
        int[] customers = Deserializer.toIntArray("[1,0,1,2,1,1,7,5]");
        int[] grumpy = Deserializer.toIntArray(   "[0,1,0,1,0,1,0,1]");
        log.info("{}", s.maxSatisfied(customers, grumpy, input));

    }

    static class Solution {
        public int maxSatisfied(int[] customers, int[] grumpy, int X) {
            int windowValue = 0;
            for (int i = 0; i<= X - 1; i ++) {
                windowValue += customers[i];
            }
            int leftProfit = 0;
            int rightProfit = 0;
            for (int i = X + 1; i  <customers.length; i ++) {
                rightProfit += grumpy[i] == 0? customers[i] : 0;
            }

            // traverse the window
            for (int i = 1; i< (customers.length - X + 1); i ++) {
                int newLeftProfit = (grumpy[i - 1] == 0 ? customers[i-1] : 0 ) + leftProfit;
                int newRightProfit = (grumpy[i+X-1] == 0 ? rightProfit - customers[i+X-1] : rightProfit );
                int newWindowProfit = windowValue + customers[i+X-1] - customers[i-1];

                if ( newLeftProfit + newWindowProfit + newRightProfit > leftProfit + windowValue + rightProfit) {
                    windowValue = windowValue + customers[i+X-1] - customers[i-1];
                    leftProfit = newLeftProfit;
                    rightProfit = newRightProfit;
                }
            }
            return leftProfit + windowValue + rightProfit;
        }
    }
}
