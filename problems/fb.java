// Given a list of coordinates, e.g.:

// [(0, 1), (1, -1), (2, 1), (-1, 0)]

// [(3, 1), (1, -1), (2, 1), (-1, 0)]

// and a k value e.g.:

// k = 2
  
// Return the k nearest coordinates to the origin (0,0)

// ex. [(0, 1), (-1, 0)] 

// O(n) * (log(k))
// space k

int[] origin = {0,0};

Queue<int[]> nearest(int[][] coordinates, int k) {
  Queue<int[]> maxHeap = new PiorityQueue<>((o1, o2) -> Double.compareTo(distance(origin,o2), distance(origin,o1) ));
  
  for (int[] point: coordinates) {
    if (maxHeap.size() < k) {
      maxHeap.offer(point);
    } else {
      int[] maxCoord = maxHeap.peek();
      double current = distance(origin, point);
      double maxDist = distance(origin, maxCoord);
      if (current < maxDist) {
        maxHeap.poll();
        maxHeap.offer(point);
      }
    }
  }
  return maxHeap;
}


// sqrt((x1 - x2) ^2 + (y1 - y2)^2)
double distance(int[] point1, int[] point2) {
  return Math.sqrt( Math.pow(point1[0] - point1[0], 2) + Math.pow(point1[1] - point1[1], 2));
}









// Given a string that looks like:

// "1212"
// "1212456789978"
  
// and a target

// t = 9
  
// Return all string combinations that sum to target, using symbols "+" and "-"
  
// e.g.
// "12-1-2"
// "-1-2+12"


// ix = 1 , acc = 1, prefix = "1"
//  "1" 
//  

// "+2"
// "-2"

class Combinations {
  List<String> results = new ArrayList<>();
  
  List<String> generateSolutions(String input, int target){
    combine(input, target, "", 0, 0);
    return results;
  }
  
  
  //O(n!)
  //2^n
  void combine(String input, int target, String prefix, int ix, int accumulator) {
    if (ix == input.length && accumulator == target) {
      results.add(prefix);
      return;
    }
    
    for (int i = ix; i<input.length; i++) {
      String strNumber = input(ix, i+1);
      int number = Integer.parseInt(strNumber);
      // addition
      if (prefix.equals("")) {
        combine(input, target, prefix+strNumber, ix + 1, number);
      } else {
        combine(input, target, prefix + "+" + strNumber, ix + 1, accumulator + number);
      }
      // subtraction
      combine(input, target, prefix + "-" + strNumber, ix + 1, accumulator - number);
    }
  }
}

// e.g.
// "12-1-2"
// "-1-2+12"
// "1+2+1+2"



