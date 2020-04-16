package othon.org.leetcode;

import java.util.ArrayList;
import java.util.List;

public class PascalTriangle_Kth_row {
    public static void main(String[] args) {
        Solution s = new Solution();
        List<Integer> r = s.getRow(1);
        r = s.getRow(2);
        r = s.getRow(3);
        System.out.println(r);
    }

    static class Solution {
        public List<Integer> getRow(int rowIndex) {
            List<Integer> result = new ArrayList<>(rowIndex + 1);
            result.add(1);
            getRow2(rowIndex, result);
            return result;
        }

        /**
         * Pascal solution using a top-down approach and memoization
         * @param rowIndex
         * @param result
         * @return
         */
        Integer getRow2(int rowIndex, List<Integer> result) {
            if (rowIndex == 0) {
                return 1;
            }
            if (rowIndex < 0) {
                return 0;
            }
            if (rowIndex<result.size() && result.get(rowIndex) != null) {
                return result.get(rowIndex);
            }
            for (int i = 1; i < rowIndex; i++) {
                int pt = getRow2(i-1, result) + getRow2(i, result);
                result.set(i, pt);
            }
            result.add(1);
            return result.get(rowIndex);
        }
    }
}
