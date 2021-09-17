package othon.org.fundamentals.misc;

public class BasicBitManipulation {

    public static void main(String[] args) {
        String s1 = "hello";
        int v = 0;
        for(int i=0; i < s1.length(); i++) {
            v |= 1 << s1.charAt(i) - 'a';
            System.out.println(v);
        }
        String s2 = "world";
        for(int i=0; i < s2.length(); i++) {
            char c = s2.charAt(i);
            int pos = c - 'a';
            if ((v & (1 << pos )) != 0) {
                System.out.println(v);
            }
        }
    }
}
