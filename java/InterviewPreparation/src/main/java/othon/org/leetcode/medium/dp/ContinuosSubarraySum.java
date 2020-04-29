package othon.org.leetcode.medium.dp;

import lombok.extern.slf4j.Slf4j;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * https://leetcode.com/problems/continuous-subarray-sum
 *
 * Todo:
 * - try bottoms up
 * - check why negative value didn't work
 */
@Slf4j
public class ContinuosSubarraySum {

    public static void main(String[] args) {
        Solution s = new Solution();
        boolean exist = s.checkSubarraySum(new int[]{23,2,4,6,7}, 6);
        log.info("Exist {}", exist);
    }

    static class Solution {
        public boolean checkSubarraySum(int[] nums, int k) {
            Map<Integer, Boolean> map = new HashMap<>();
            List<Integer> numbers = new ArrayList<Integer>();
            numbers.add(nums[nums.length - 1]);
            return check(nums, nums.length - 2, map, k, numbers);
        }

        boolean check(int[] nums, int ix, Map<Integer, Boolean> map, int k, List<Integer> sub) {
            log.info("ix {}->[{}]", ix, sub);
            if (ix < 0 ) {
                return false;
            }
            int result = 0;
            sub.add(nums[ix]);
            int n = sub.size();
            for (int i=0; i<n &&  n>=2;result += sub.get(i++));
            if (n >=2 && ((k != 0 && result % k ==0) || (k==0 && result == 0))) {
                map.put(result, true);
                return true;
            }
            if (map.containsKey(result)) {
                return map.get(result);
            }
            List<Integer> newList = new ArrayList<>();
            newList.add(nums[ix]);
            boolean found = check(nums, ix - 1, map, k, sub) || check(nums, ix - 1, map, k, newList)
                    || check(nums, ix - 1, map, k, new ArrayList<>());
            map.put(result, found);

            return map.get(result);
        }

        boolean check2(int[] nums, int ix, Map<Integer, Boolean> map, int k, Integer sub) {
            log.info("ix {}->[{}]", ix, sub);
            if (ix < 0 ) {
                return false;
            }
            int result = 0;
            if (sub!= null) {
                sub += nums[ix];
                result = sub;
                if ((k != 0 && result % k ==0) || (k==0 && result == 0)) {
                    map.put(result, true);
                    return true;
                }
            } else {
                result = nums[ix];
            }
            if (sub!= null && map.containsKey(result)) {
                return map.get(result);
            }


            List<Integer> newList = new ArrayList<>();
            newList.add(nums[ix]);
            boolean found = check2(nums, ix - 1, map, k, sub) || check2(nums, ix - 1, map, k, nums[ix])
                    || check2(nums, ix - 1, map, k, null);
            map.put(result, found);

            return map.get(result);
        }
    }
}
