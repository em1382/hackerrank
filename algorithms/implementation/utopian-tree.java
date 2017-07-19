import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int cases = sc.nextInt();
		int height;
		int cycles;

		for (int i = 0; i < cases; i++) {
			height = 1;
			cycles = sc.nextInt();

			for (int j = 0; j < cycles; j++) {
				if (j % 2 == 0) {
					height = height * 2;
				} else {
					height += 1;
				}
				
			}
			
			System.out.println(height);
		}

		sc.close();
	}
}
