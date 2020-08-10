package othon.org.leetcode.medium.array;

import java.util.Comparator;
import java.util.PriorityQueue;

/**
 * You want tot make  a roadtrip but want to spend the minimum amount of gas, how would you do that?
 * Link: https://leetcode.com/problems/minimum-number-of-refueling-stops/solution/
 */
public class TipFromSeattleToBoston {


    public static void main(String[] args) {
        double[] gasPrices = {1.2, 2.0, 3.5, 1.2, 2.3, 8.3, 5.6};
        double[] gasPricesByMile = {1.2, 2.0, 3.5, 1.2, 2.3, 8.3, 5.6};
        int capacity = 3;
        //double minGas = calculateGas(gasPrices, capacity, 0);

    }

    // Option 1: Using Brute force
    // Time complexity: O(N x Capacity)
    // Space complexity: O (1)
    private static double bruteForce_wrong(double[][] gasPrices, int capacity, int currentTank) {
        double totalGasCost = 0.0;

        int mileLastGasStation = Integer.MIN_VALUE;

        for (int i = 0; i < gasPrices.length; i++) {
            double smallestPrice = Double.MAX_VALUE;
            int mile = (int) gasPrices[i][0];
            int currentMile = mile;
            for (int j = i; j < capacity; j++) {
                for (int k = 1; k < gasPrices[j].length; k++) {
                    if (gasPrices[j][k] < smallestPrice) {
                        smallestPrice = gasPrices[j][k];
                        mile = (int) gasPrices[i][0];
                    }
                }
            }

            // calculate the distance to the next gas station where we are charging gas
            int newGasStationInMiles = mile - currentMile;
            int gasToBuyInMiles = newGasStationInMiles - currentTank;
            double gasBought = smallestPrice * gasToBuyInMiles;
            currentTank = gasToBuyInMiles;
            totalGasCost += gasBought;
        }
        return totalGasCost;
    }
//    private static double bruteForce(double[][] gasPrices, int capacity, int currentTank) {
//        double totalGasCost = 0.0;
//
//        int mileToBuyGas = Integer.MIN_VALUE;
//        int n = gasPrices.length;
//        for (int i = 0; i < gasPrices.length; i++) {
//            double smallestPrice = Double.MAX_VALUE;
//            int mile = (int)gasPrices[i][0];
//
//            double reachablePriceWithCurrentTank = Double.MAX_VALUE;
//            int reachableMileWithCurrentTank = (int)gasPrices[i][0];
//
//            int currentMile = mile;
//
//
//            for (int j = i; j < capacity + 1 && j < n; j++) {
//                for (int k = 1; k < gasPrices[j].length; k++) {
//                    if (gasPrices[j][k] < smallestPrice) {
//                        smallestPrice = gasPrices[j][k];
//                        mile = (int)gasPrices[i][0];
//                    }
//                }
//                if (j <= i + currentTank && smallestPrice < reachablePriceWithCurrentTank) {
//                    reachablePriceWithCurrentTank = smallestPrice;
//                    reachableMileWithCurrentTank = mile;
//                }
//            }
//
//            // calculate the distance to the next gas station where we are charging gas
//            // but only if the new mile is from a different gas station.
//            if (mileToBuyGas == i) {
//                int newGasStationInMiles = mile - currentMile;
//                int gasToBuyInMiles = newGasStationInMiles - currentTank;
//                double gasBought = smallestPrice * gasToBuyInMiles;
//                currentTank += gasToBuyInMiles;
//                totalGasCost += gasBought;
//                mileToBuyGas = mile;
//            }
//            currentTank -= 1;
//        }
//        return totalGasCost;
//    }

    /*
        // Time complexity: O(N x TankCapacity)
        // Space complexity: O (1)
     */
    private static double bruteForce(double[][] gasPrices, int tankCapacity, int currentTank) {
        double totalGasCost = 0.0;

        int mileToBuyGas = Integer.MIN_VALUE;

        for (int i = 0; i < gasPrices.length; i++) {
            double smallestPrice = Double.MAX_VALUE;
            int mile = (int) gasPrices[i][0];
            int currentMile = (int) gasPrices[i][0];

            for (int j = i; j < currentTank; j++) {
                for (int k = 1; k < gasPrices[j].length; k++) {
                    if (gasPrices[j][k] < smallestPrice) {
                        smallestPrice = gasPrices[j][k];
                        mileToBuyGas = (int) gasPrices[j][0];
                    }
                }
            }

            if (mileToBuyGas == i) {
                smallestPrice = Double.MAX_VALUE;
                // find the next gas station that we can fill up the gas tank
                for (int j = i; j < tankCapacity; j++) {
                    for (int k = 1; k < gasPrices[j].length; k++) {
                        if (gasPrices[j][k] < smallestPrice) {
                            smallestPrice = gasPrices[j][k];
                            mile = (int) gasPrices[j][0];
                        }
                    }
                }

                // calculate the distance to the next gas station where we are charging gas
                int nextGasStationInMiles = mile - currentMile;
                double gasBought = smallestPrice * nextGasStationInMiles;
                currentTank = nextGasStationInMiles;
                totalGasCost += gasBought;
            } else {
                currentTank -= 1;
            }
        }
        return totalGasCost;
    }

    /*
       // Time complexity: O(N x TankCapacity)
       // Space complexity: O (1)
       Even when the new algorithm is "leaping" jumping, the nested for loop still makes it O(N x TankCapacity)
    */
    private static double bruteForceImproved(double[][] gasPrices, int tankCapacity, int currentTank) {
        int n = gasPrices.length;

        // first: find the cheapeast gas station that we can stop by with the current tank
        double smallestPrice = Double.MAX_VALUE;
        int nextGasStationInMiles = (int) gasPrices[0][0];

        for (int j = 0; j <= currentTank && j < n; j++) {
            for (int k = 1; k < gasPrices[j].length; k++) {
                if (gasPrices[j][k] < smallestPrice) {
                    smallestPrice = gasPrices[j][k];
                    nextGasStationInMiles = (int) gasPrices[j][0];
                }
            }
        }
        double totalGasCost = smallestPrice * (nextGasStationInMiles - currentTank);
        int left = nextGasStationInMiles;

        while (left < n) {
            for (int j = left; j < tankCapacity; j++) {
                for (int k = 1; k < gasPrices[j].length; k++) {
                    if (gasPrices[j][k] < smallestPrice) {
                        smallestPrice = gasPrices[j][k];
                        nextGasStationInMiles = (int) gasPrices[j][0];
                    }
                }
            }
            totalGasCost = smallestPrice * (nextGasStationInMiles - left);
            left = nextGasStationInMiles;
        }
        return totalGasCost;
    }

    // Option 2: Using dp
    // Decide to take the gas at a given point or not depending if the price is cheaper
    // however this option is not optimal. Doesn't improve time complexity and requires
    // a space complexity of O(N x Tank)


    // Option 3: Using sliding window
    // Step 1: first find the chepeast gas under the capacity:
    // step 2: get how many miles are up to it. each position in the array is a mile.
    // Step 3: from the new gas station, save the price and find the new chepeast gas station that we can reach with our tank
    // Step 4: decide how much gas to buy to reach the new chepeast gas station.
    // Time complexity O(n)
    private static double slidingWindow(double[][] gasPrices, int tankCapacity, int currentTank) {
        int n = gasPrices.length;
        PriorityQueue<double[]> minHeap = new PriorityQueue<>(Comparator.comparingDouble(o -> o[0])); // 0 = price, 1 = mile

        double totalGasCost = 0;
        for (int i = 0; i < n; i++) {
            if (i > 0 && (i % tankCapacity == 0 || i == n-1)) {
                // calculate price
                int delta = tankCapacity - currentTank;
                while (delta > 0 ) {
                    double[] gasStation = minHeap.poll();
                    int dist = tankCapacity - (int)gasStation[1];
                    if (dist <= currentTank) { // for the initial case
                        totalGasCost += delta * gasStation[0];
                    } else {
                        totalGasCost += dist * gasStation[0];
                        delta -= dist;
                    }
                }
                if (currentTank > 0) { // for the intial case
                    currentTank = 0;
                }
                minHeap.clear();
            }
            double smallestPrice = Double.MAX_VALUE;
            double nextGasStationInMiles = gasPrices[i][0];
            for (int k = 1; k < gasPrices[i].length; k++) {
                if (gasPrices[i][k] < smallestPrice) {
                    smallestPrice = gasPrices[i][k];
                    nextGasStationInMiles = gasPrices[i][0];
                }
            }
            minHeap.offer(new double[]{smallestPrice, nextGasStationInMiles});
        }
        return totalGasCost;
    }


    static class TestCase {
        static TestCase[] scenarios = {
                new TestCase(new double[][]{{1, 1.0, 2.3, 3.5},
                        {2, 1.0, 2.3, 3.5},
                        {3, 1.1, 2.3, 3.5},
                        {4, 1.3, 2.3, 3.5},
                        {5, 1.5, 2.3, 3.5},
                        {6, 1.7, 2.3, 3.5},
                        {7, 1.9, 2.3, 3.5},
                        {8, 2.1, 2.3, 3.5},
                        {9, 2.4, 2.3, 3.5},
                        {10, 2.9, 2.3, 3.5},
                        {11, 3.4, 2.3, 3.5},
                        {12, 4.0, 3.8, 3.5},
                }, 1, 3)
        };
        double[][] stations;
        int currentTank;
        int capacity;

        public TestCase(double[][] stations, int currentTank, int capacity) {
            this.stations = stations;
            this.currentTank = currentTank;
            this.capacity = capacity;
        }


    }
}
