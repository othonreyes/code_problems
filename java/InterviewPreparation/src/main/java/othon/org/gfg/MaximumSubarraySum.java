package othon.org.gfg;
//https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/
public class MaximumSubarraySum {
    public static void main(String[] args) {
        int arr[] = {-2, -5, 6, -2, -3, 1, 5, -6};
        int n = arr.length;
        int max_sum = maxSubArraySum(arr, 0, n-1);

        System.out.println("Maximum contiguous sum is "+
                max_sum);
    }

    private static int maxSubArraySum(int[] arr, int left, int right) {
        if (left == right) {
            return arr[left];
        }
        int mid = (left + right) / 2;
        return Math.max(
                Math.max(maxSubArraySum(arr, left, mid),
                        maxSubArraySum(arr, mid + 1, right)),
                middleSum(arr, left, mid, right)
        );
    }

    // The trick is that in the merge, you traverse the array from the middle to the extremes i.e. left or right!!
    private static int middleSum(int[] arr, int left, int mid, int right) {
        int leftSum = Integer.MIN_VALUE;
        int sum = 0;
        for (int i = mid; i>= left; i--) {
            sum += arr[i];
            if (sum > leftSum)
                leftSum = sum;
        }

//        int rightSum = Integer.MIN_VALUE;
//        sum = 0;
//        for (int i = right; i> mid; i--) {
//            sum += arr[i];
//            if (sum > rightSum)
//                rightSum = sum;
//        }
        sum = 0;
        int rightSum = Integer.MIN_VALUE;
        for (int i = mid + 1; i <= right; i++) {
            sum += arr[i];
            if (sum > rightSum)
                rightSum = sum;
        }
        return Math.max(leftSum + rightSum, Math.max(leftSum, rightSum));
    }
}
