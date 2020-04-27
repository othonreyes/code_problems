package othon.org.fundamentals.sorting;

import lombok.extern.slf4j.Slf4j;

@Slf4j
public class QuickSort {

    public static void main(String[] args) {
        int[] arr = new int[]{5,8,3,6,1,4,9,7,2};
        quicksort(arr, 0 , arr.length - 1);
        log.info("{}",arr);
    }

    private static void quicksort(int[] arr, int left, int right) {
        log.info("{}",arr);
        int index = partition(arr, left, right);
        if (left < index - 1) {
            quicksort(arr, left, index-1);
        }
        if (index < right) {
            quicksort(arr, index, right);
        }
    }

    private static int partition(int[] arr, int left, int right) {
        int pivot = arr[left + (right - left) / 2];
        while (left <= right) {
            while(arr[left]<pivot) left++;

            while(arr[right] > pivot)
                right--;

            if (left <= right) {
                // swap
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                left ++;
                right --;
            }
        }
        return left;
    }
}
