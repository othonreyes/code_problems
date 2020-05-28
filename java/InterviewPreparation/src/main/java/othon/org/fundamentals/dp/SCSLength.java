package othon.org.fundamentals.dp;

// https://www.techiedelight.com/shortest-common-supersequence-introduction-scs-length/
public class SCSLength {
    // Function to find length of shortest Common supersequence of
    // sequences X[0..m-1] and Y[0..n-1]
    public static int SCSLength(String X, String Y, int m, int n)
    {
        // if we have reached the end of either sequence, return
        // length of other sequence
        if (m == 0 || n == 0) {
            return n + m;
        }

        // if last character of X and Y matches
        if (X.charAt(m - 1) == Y.charAt(n - 1)) {
            return SCSLength(X, Y, m - 1, n - 1) + 1;
        }

        // last character of X and Y don't match
        return Integer.min(SCSLength(X, Y, m, n - 1) + 1,
                SCSLength(X, Y, m - 1, n) + 1);
    }

    // main function
    public static void main(String[] args)
    {
        String X = "ABCBDAB", Y = "BDCABA";
        int m = X.length(), n = Y.length();

        System.out.print("The length of shortest Common supersequence is "
                + SCSLength(X, Y, m, n));
    }
}
