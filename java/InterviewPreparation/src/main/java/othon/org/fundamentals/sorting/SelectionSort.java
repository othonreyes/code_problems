package othon.org.fundamentals.sorting;

import lombok.extern.slf4j.Slf4j;
import othon.org.utils.SortingUtils;

import java.util.Arrays;

@Slf4j
public class SelectionSort {
    public static void main(String[] args) {
        int[] arr = SortingUtils.createUnorderedArray();
        log.info("{}", arr);

        int[] arr2 = Arrays.copyOf(arr, arr.length);
        long startTime = System.nanoTime();
        selectionSort(arr2);
        log.info("selectionSort {}- {}", arr2, System.nanoTime() - startTime);

        arr2 = Arrays.copyOf(arr, arr.length);
        startTime = System.nanoTime();
        mergeSort(arr2);
        log.info("mergeSort {}- {}", arr2, System.nanoTime() - startTime);

        arr2 = Arrays.copyOf(arr, arr.length);
        startTime = System.nanoTime();
        quickSort(arr2);
        log.info("quickSort {}- {}", arr2, System.nanoTime() - startTime);
    }

    /**
     * Find the smallest element in the array and swap it at the begining of the array.
     * Continue that way until all elements are covered
     * T: O(n^2)
     * S: O(1)
     * @param arr
     */
    private static void selectionSort(int[] arr) {
        int i = 0;
        while ( i < arr.length) {
            int smallest = arr[i];
            int ix = i;
            for (int j=i +1; j<arr.length; j++ ) {
                if (arr[j]<smallest) {
                    smallest = arr[j];
                    ix = j;
                }
            }
            if (smallest < arr[i]) {
                int temp = arr[i];
                arr[i] = smallest;
                arr[ix] = temp;
            }
            i +=1;
        }
    }



    private static void mergeSort(int[] arr) {
        int[] helper = new int[arr.length];
        mergeSort(arr, helper, 0, arr.length - 1);
    }

    private static void mergeSort(int[] arr, int[] helper, int left, int right) {
        if (left < right) {
            int middle = left  + (right -left)/2;
            mergeSort(arr, helper, left, middle);
            mergeSort(arr, helper, middle + 1, right);
            merge(arr, helper, left, middle, right);
        }
    }

    private static void merge(int[] arr, int[] helper, int left, int middle, int right) {
        // first, copy the values to the helper
        for (int i = left; i<= right; i++) {
            helper[i] = arr[i];
        }
        int helperLeft = left;
        int helperRight = middle + 1;
        int current = left;
        while (helperLeft<=middle && helperRight <= right) {
            if (helper[helperLeft]<=helper[helperRight]) {
                arr[current] = helper[helperLeft];
                helperLeft += 1;
            } else {
                arr[current] = helper[helperRight];
                helperRight += 1;
            }
            current += 1;
        }

        int remaining = middle - helperLeft;
        for (int i = 0; i<=remaining; i++) {
            arr[current + i] = helper[helperLeft + i];
        }
    }

    private static void quickSort(int[] arr) {
        quickSort(arr, 0, arr.length - 1);
    }

    private static void quickSort(int[] arr, int left, int right) {
        int index = partition(arr, left, right);
        if (left<index-1) {
            quickSort(arr, left, index -1);
        }
        if (index < right) {
            quickSort(arr, index, right);
        }
    }

    private static int partition(int[] arr, int left, int right) {
        int pivot = arr[left + (right-left) / 2];
        while (left<=right) {
            //move left
            while (arr[left] < pivot) left+=1;
            // move right
            while (arr[right] > pivot) right -=1;
            // compare indexes
            if (left<=right) {
                // swap
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                left += 1;
                right -= 1;
            }
        }
        return left;
    }
}
