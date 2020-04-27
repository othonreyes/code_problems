package othon.org.leetcode;

import lombok.extern.slf4j.Slf4j;

import java.util.Arrays;

@Slf4j
public class MultiplyString {

    public static void main(String[] args) {
        Solution s = new Solution();
        log.info("{}", s.multiply("2", "3"));
        log.info("{}", s.multiply("123", "456"));
        log.info("{}", s.multiply("9", "9"));
    }
    static class Solution {
        public String multiply(String num1, String num2) {
            if (num1.length() > num2.length()) {
                return multp(num1, num2);
            } else {
                return multp(num2, num1);
            }
        }
        String multp(String largest, String shortest){
            char[] result = new char[largest.length() + shortest.length()];
            //Init the result int array
            for (int i=0 ; i < result.length ; i++) {
                result[i] = '0';
            }

            int n = result.length;
            int k = 0;
            int j = shortest.length() - 1;
            int co = 0;
            while (j>=0) {
                k = --n;
                co = 0;
                int i = largest.length() - 1;
                while (i>=0) {
                    int val = (largest.charAt(i)-'0') * (shortest.charAt(j)-'0') + co;
                    val = val + (result[k]-'0');
                    result[k] = (char) ('0' + val % 10);
                    co = val / 10;
                    i-=1;
                    k-=1;
                }
                result[k] = (char) ('0' + co % 10);
                j-=1;
            }

            // add last carryover
            if (k >=0 && co > 0)
                result[k] = (char) ('0' + co);
            else k+=1;

            //search for the last 0. need to do it in reverse order
//            int start = 0;
//            for (int i = result.length-1; i>=0 &&result[i]; i++)
//                if (result[i]=='0')
//                    start = i;
//                else
//                    break;
//            start = start == n?start -1:start+1;
            return new String(Arrays.copyOfRange(result,k, result.length));
        }
    }
//    public String multiply(String num1, String num2) {
//        if(num1.equals("0") || num2.equals("0")) return "0";
//        int[] digits = new int[num1.length()+num2.length()];
//        for(int i=num2.length()-1;i>=0;i--){
//            int pos = (num2.length()-1)-i;
//            int carry=0;
//            for(int j=num1.length()-1;j>=0;j--){
//                int digit = (num2.charAt(i)-'0') * (num1.charAt(j)-'0');
//                carry = digit/10;
//                digit%=10;
//                digits[pos]+=digit;
//                digits[pos+1]+=carry;
//
//                pos++;
//            }
//        }
//
//        StringBuilder sb = new StringBuilder();
//        int i=digits.length-1;
//        while(i>=0 && digits[i]==0) i--;
//        int carry=0;
//        for(int j=0;j<=i;j++){
//            digits[j]+=carry;
//            carry = digits[j]/10;
//            if(j!=i) digits[j]%=10;
//        }
//        for(int j=i;j>=0;j--){
//            sb.append(digits[j]);
//        }
//        return sb.toString();
//    }


}
