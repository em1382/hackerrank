import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
        int arrSize = sc.nextInt();
        long total = 0;
        
        for(int i = 0; i < arrSize; i++) {
            total += sc.nextLong();
        }

        System.out.println(total);
    }
}
