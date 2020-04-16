package othon.org.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

public class ThreeSum_15 {

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] input = {-1, 0, 1, 2, -1, -4};

        print(s.threeSum(input));
        System.out.println();
        print(s.threeSumSorting(input));
        System.out.println();
        print(s.threeSum2Pointer(input));
    }

    private static void print(List<List<Integer>> check) {
        check.stream().forEach(l -> System.out.println(l
                .stream()
                .map(i->String.valueOf(i) + ",")
                .collect(Collectors.joining())
        ));
    }

    static class Solution {
        public List<List<Integer>> threeSum(int[] nums) {
            if (nums.length<3) {
                return new ArrayList<List<Integer>>();
            }
//            List<List<Integer>> results = new ArrayList<>();
            Set<List<Integer>> results = new HashSet<>(); // use a set to avoid duplicates
            // needs sorting to about mixing the results
            for (int i=0; i< nums.length; i++) {
                int target = nums[i];
                twoSum(nums, target, i + 1, results);
            }
            return new ArrayList<>(results);
        }

        void twoSum(int[] nums, int target, int start, Set<List<Integer>> results) {
            Map<Integer, Integer> map = new HashMap<>();
            for (int i = start; i<nums.length; i++) {
                int delta = -1 * target - nums[i];
                if (map.get(delta) != null) {
                    results.add(Arrays.asList(target, nums[i], nums[map.get(delta)]));
                } else {
                    map.put(nums[i], i);
                }
            }
        }

        public List<List<Integer>> threeSumSorting(int[] nums) {
            if (nums.length<3) {
                return new ArrayList<List<Integer>>();
            }
            Arrays.sort(nums);
            Set<List<Integer>> results = new HashSet<>(); // use a set to avoid duplicates
            for (int i=0; i< nums.length; i++) {
                int target = nums[i];
                twoSum(nums, target, i + 1, results);
            }
            return new ArrayList<>(results);
        }

        public List<List<Integer>> threeSum2Pointer(int[] nums) {
            if (nums.length<3) {
                return new ArrayList<List<Integer>>();
            }
            Arrays.sort(nums);
            Set<List<Integer>> results = new HashSet<>(); // use a set to avoid duplicates
            for (int i=0; i< nums.length; i++) {
                int left = i + 1;
                int right = nums.length - 1;
                int total = 0;
                while (left < right) {
                    total = nums[i] + nums[left] +  nums[right];
                    if (total > 0) {
                        right -= 1;
                    } else if (total < 0) {
                        left += 1;
                    } else {
                        results.add(Arrays.asList(nums[i], nums[left], nums[right]));
                        // moving pointers so we don't repeat them
                        left += 1;
                        right -= 1;
                    }
                }

            }
            return new ArrayList<>(results);
        }
    }
}
