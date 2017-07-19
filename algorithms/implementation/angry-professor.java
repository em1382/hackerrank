import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n, k;
		int cases = sc.nextInt();
		
		for (int i = 0; i < cases; i++) {
			n = sc.nextInt();
			k = sc.nextInt();
						
			int onTime = 0;
			
			for (int j = 0; j < n; j++) {				
				if (sc.nextInt() <= 0) {
					onTime++;						
				}
			}
						
			if (onTime >= k) {
				System.out.println("NO");
			} else {
				System.out.println("YES");
			}
		}
		
		sc.close();
	}
}
