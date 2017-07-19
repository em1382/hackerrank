import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int width = scanner.nextInt();
        int[][] array = new int[width][width];
        for (int i = 0; i < width; i++) {
            for (int j = 0; j < width; j++) {
                array[i][j] = scanner.nextInt();
                //System.out.println(array[i][j]);
            }
        }
        
        int total1 = 0, total2 = 0;
        
        for (int k = 0; k < width; k++) {
            total1 += array[k][k];
            total2 += array[k][width - k - 1];
        }
        
        System.out.println(Math.abs(total1 - total2));
    }
}
