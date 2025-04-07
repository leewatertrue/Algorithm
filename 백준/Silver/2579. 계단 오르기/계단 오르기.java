import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt(); 
        int stair[]=new int[n];
        for (int i = 0; i < n; i++) {
            stair[i] = s.nextInt();
        }
        int[] dp = new int[n];
        for (int i = 0; i < n; i++) { 
            if(i==0) {
            	dp[0]=stair[0];
            } else if (i==1) {
            	dp[1] = Math.max(stair[0] + stair[1], stair[1]);
            } else if (i==2) {
            	dp[2] = Math.max(stair[1] + stair[2], dp[0] + stair[2]);
            } else {
            	dp[i] = Math.max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i]);
            }
        }
        System.out.println(dp[n-1]);
    }
}