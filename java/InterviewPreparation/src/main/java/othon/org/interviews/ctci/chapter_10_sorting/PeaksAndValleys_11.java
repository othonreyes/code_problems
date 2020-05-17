package othon.org.interviews.ctci.chapter_10_sorting;

import lombok.extern.slf4j.Slf4j;

import java.util.Arrays;

@Slf4j
public class PeaksAndValleys_11 {

    public static void main(String[] args) {
        int [] arr = new int[]{1,5,8,3,4,6,5,2,1,3,5,6,7,9,6,1,3};
        int [] arr2 = Arrays.copyOf(arr, arr.length);
        log.info("{}", arr);
        sort_ctci(arr2);
        log.info("{}", arr2);

        sort_me(arr2);
        log.info("{}", arr2);
    }

    private static void sort_me(int[] arr) {
        // copy
        int[] helper = Arrays.copyOf(arr, arr.length);

        if(!sort(arr, helper, false)){
            helper = Arrays.copyOf(arr, arr.length);
            sort(arr, helper, true);
        }
        // copy the results
        arr = Arrays.copyOf(helper, helper.length);
    }

    private static boolean sort(int[] arr, int[] helper, boolean valley) {
        for (int i = 1; i < helper.length; i++) {
            Integer ix = findNext(arr, i + 1, !valley);
            if (ix == null) {
                //no solution
                return false;
            }
            swap(helper, i, ix);
            valley = !valley;
        }
        return true;
    }

    private static Integer findNext(int[] arr, int i, boolean valley) {
        if (i == arr.length) {
            return null;
        }
        for (int j = 0; j < arr.length; j++) {
            if (valley && arr[i-1]>=arr[j]) {
                return arr[j];
            } else if (valley && arr[i-1]<=arr[j]) {
                return arr[j];
            }
        }
        return null;
    }


    private static void sort_ctci(int[] arr) {
        for (int i = 1; i<arr.length; i+=2) {
            int biggestIx = biggestIx(arr, i- 1, i , i+1);
            swap(arr, i, biggestIx);
        }
    }

    private static void swap(int[] arr, int i, int biggestIx) {
        int temp = arr[i];
        arr[i] = arr[biggestIx];
        arr[biggestIx] = temp;
    }

    private static int biggestIx(int[] arr, int a, int b, int c) {
        int av = arr[a];
        int bv = arr[b];
        int cv = c<arr.length? arr[c] : Integer.MIN_VALUE;
        int max = Math.max(av, Math.max(bv,cv));
        if (max == av) return a;
        if (max == bv) return b;
        return c;
    }
}
