package othon.org.fundamentals.sorting;

import lombok.extern.slf4j.Slf4j;
import othon.org.utils.SortingUtils;

@Slf4j
public class MergeSort {
    public static void main(String[] args) {
        int[] arr = SortingUtils.createUnorderedArray(20, 10000);
        int[] helper = new int[arr.length];
        mergesort(arr, helper, 0, arr.length - 1);
        log.info("{}", arr);
    }

    private static void mergesort(int[] arr, int[] helper, int left, int right) {
        if (left < right) {
            log.info("{}", arr);
            int middle = left + (right - left) / 2;
            mergesort(arr, helper, left, middle);
            mergesort(arr, helper, middle + 1, right);
            merge(arr, helper, left, middle, right);
        }
    }

    private static void merge(int[] arr, int[] helper, int left, int middle, int right) {
        for (int i = left; i <= right; i++) {
            helper[i] = arr[i];
        }

        int helperLeft = left;
        int helperRight = middle + 1;
        int current = left;
        while (helperLeft <= middle && helperRight <= right) {
            if (helper[helperLeft] <= helper[helperRight]) {
                arr[current] = helper[helperLeft];
                helperLeft += 1;
            } else {
                arr[current] = helper[helperRight];
                helperRight += 1;
            }
            current += 1;
        }

        // copy lst elements from the left
        int remaining = middle - helperLeft;
        for (int i = 0; i <= remaining; i++) {
            arr[current + i] = helper[helperLeft + i];
        }
    }
}

