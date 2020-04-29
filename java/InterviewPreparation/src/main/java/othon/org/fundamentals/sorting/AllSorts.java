package othon.org.fundamentals.sorting;

import lombok.extern.slf4j.Slf4j;

import java.util.Arrays;



@Slf4j
public class AllSorts {
    public static void main(String[] args) {
        int[] arr = SortingUtils.createUnorderedArray(20, 10000);
        log.info("{}", arr);
        int[] arr2 = Arrays.copyOf(arr, arr.length);

        long startTime = System.nanoTime();
        mergeSort(arr2);
        log.info("mergeSort {}- {}", arr2, System.nanoTime() - startTime);

        arr2 = Arrays.copyOf(arr, arr.length);
        startTime = System.nanoTime();
        quickSort(arr2);
        log.info("quickSort {}- {}", arr2, System.nanoTime() - startTime);

        arr2 = Arrays.copyOf(arr, arr.length);
        startTime = System.nanoTime();
        countingSort(arr2);
        log.info("countingSort {}- {}", arr2, System.nanoTime() - startTime);


//        long startTime = System.nanoTime();
//        int[] arr2 = radixSort(arr2);
//        log.info("selectionSort {}- {}", arr2, System.nanoTime() - startTime);
//


    }

    private static void countingSort(int[] arr) {
        int min = Arrays.stream(arr).min().getAsInt();
        int max = Arrays.stream(arr).max().getAsInt();
        int range = max - min + 1; // +1 very important
        int[] count = new int[range];
        for (int i = 0; i < arr.length; i++) {
            count[arr[i]-min] += 1;
        }
        // carry over the sum of previous count
        for (int i = 1; i < count.length; i++) {
            count[i] += count[i-1];
        }
        int[] output = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            output[count[arr[i]-min] - 1] = arr[i];
            count[arr[i]-min] -= 1;
        }
        for (int i = 0; i < arr.length; i++) {
            arr[i] = output[i];
        }
    }

    private static void quickSort(int[] arr) {
        quickSort(arr, 0, arr.length - 1);
    }

    private static void quickSort(int[] arr, int left, int right) {
        int index = partition(arr,left, right);
        if (left<index - 1) {
            quickSort(arr, left, index - 1);
        } if (index < right) {
            quickSort(arr, index, right);
        }
    }

    private static int partition(int[] arr, int left, int right) {
        int pivot = arr[(left + right) / 2];
        while (left<=right) {
            while(arr[left]<pivot) left+=1;
            while(arr[right]> pivot) right-=1;
            if(left<=right) {
               int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                left +=1;
                right -=1;
            }
        }
        return left;
    }

    // merge sort
    private static void mergeSort(int[] arr2) {
        int[] helper = new int[arr2.length];
        mergeSort(arr2, helper, 0, arr2.length- 1);
    }

    private static void mergeSort(int[] arr2, int[] helper, int left, int right) {
        if (left<right) {
            // from here until the end all comparisons uses <=
//            int middle = left + (right-left) / 2;
            int middle = left + (right - left)/2;
            mergeSort(arr2, helper, left, middle);
            mergeSort(arr2, helper, middle + 1, right);
            merge(arr2, helper, left,middle, right);
        }
    }

    private static void merge(int[] arr2, int[] helper, int left,int middle, int right) {
        for (int i = left; i <= right; i++) {
            helper[i] = arr2[i];
        }
        int helperLeft = left;
        int helperRight = middle + 1;
        int current = left;
        while (helperLeft<=middle && helperRight<=right) {
//            if (helper[helperRight] <= helper[helperLeft]){ // descending
            if (helper[helperLeft] <= helper[helperRight]){ // ascending
                arr2[current] = helper[helperLeft];
                helperLeft += 1;
            } else {
                arr2[current] = helper[helperRight];
                helperRight += 1;
            }
            current +=1;
        }
        int remaining = middle - helperLeft;
        for (int i = 0; i <= remaining; i++) {
            arr2[current + i] = helper[helperLeft + i];
        }
    }

    // quick sort


    // count sort

    // radix sort
}
