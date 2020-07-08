package othon.org.fundamentals.sorting;

import lombok.extern.slf4j.Slf4j;
import othon.org.utils.SortingUtils;

import java.util.Arrays;


@Slf4j
public class AllSorts {
    public static void main(String[] args) {
        int[] arr = SortingUtils.createUnorderedArray(20, 10000);
        log.info("{}", arr);
        int[] arr2 = Arrays.copyOf(arr, arr.length);

        long startTime = System.nanoTime();
        mergeSort(arr2);
        log.info("mergeSort    {}- {}", arr2, System.nanoTime() - startTime);

        arr2 = Arrays.copyOf(arr, arr.length);
        startTime = System.nanoTime();
        quickSort(arr2);
        log.info("quickSort    {}- {}", arr2, System.nanoTime() - startTime);

        int[] arr3 = Arrays.copyOf(arr, arr.length);
        startTime = System.nanoTime();
        countSort(arr3);
        log.info("countingSort {}- {}", arr3, System.nanoTime() - startTime);

        int[] arr4 = Arrays.copyOf(arr, arr.length);
        startTime = System.nanoTime();
        radixSort(arr4);
        log.info("radixSort    {}- {}", arr4, System.nanoTime() - startTime);

        assert Arrays.equals(arr2, arr3);
        assert Arrays.equals(arr2, arr4);
    }

    private static void mergeSort(int[] arr) {
        int[] helper = new int[arr.length];
        mergeSort(arr, helper, 0, arr.length - 1);
    }

    private static void mergeSort(int[] arr, int[] helper, int left, int right) {
        if (left < right) {
            int middle = (left + right) / 2;
            mergeSort(arr, helper, left, middle);
            mergeSort(arr, helper, middle + 1, right);
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

    // radix sort
    static void radixSort(int[] arr) {
        int max = Arrays.stream(arr).max().getAsInt();
        for (int exp = 1; max / exp > 0; exp *= 10) {
            countSort(arr, exp);
        }
    }

    static private void countSort(int[] arr, int exp) {
        int[] count = new int[10];
        for (int i = 0; i < arr.length; i++) {
            count[(arr[i] / exp) % 10] += 1;
        }
        for (int i = 1; i < 10; count[i] += count[i++ - 1]) ;
        int[] output = new int[arr.length];
        for (int i = arr.length - 1; i >= 0; i--) { // go in reverse is very important
            output[count[(arr[i] / exp) % 10] - 1] = arr[i];
            count[(arr[i] / exp) % 10] -= 1;
        }
        for (int i = 0; i < arr.length; arr[i] = output[i++]) ;
    }


    // counting sort
    static private void countSort(int[] arr) {
        int min = Arrays.stream(arr).min().getAsInt();
        int max = Arrays.stream(arr).max().getAsInt();
        int range = max - min + 1;
        int[] count = new int[range];
        for (int i = 0; i < arr.length; i++) {
            count[arr[i] - min] += 1;
        }
        for (int i = 1; i < count.length; count[i] += count[i++ - 1]) ;
        int[] output = new int[arr.length];
        for (int i = arr.length - 1; i >= 0; i--) {
            output[count[arr[i] - min] - 1] = arr[i];
            count[arr[i] - min] -= 1;
        }
        for (int i = 0; i < arr.length; arr[i] = output[i++]) ;
    }

    // quick sort
    static private void quickSort(int[] arr) {
        quickSort(arr, 0, arr.length - 1);
    }

    private static void quickSort(int[] arr, int left, int right) {
        int index = partition(arr, left, right);
        if (left < index - 1) {
            quickSort(arr, left, index - 1);
        }
        if (index < right) {
            quickSort(arr, index, right);
        }
    }

    private static int partition(int[] arr, int left, int right) {
        int pivot = arr[(left + right) / 2];
        while (left <= right) {
            while (arr[left] < pivot) left += 1;
            while (arr[right] > pivot) right -= 1;
            if (left <= right) {
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                left += 1;
                right -= 1;
            }
        }
        return left;
    }


    // counting sort
    // selection sort
    // insert sort
    // pancake sort
    // bubble sort
}
