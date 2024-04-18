import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	static int[][] dp = new int[10001][4];

	static void solution() {
		dp[1][1] = dp[2][1] = dp[2][2] = dp[3][1] = dp[3][2] = dp[3][3] = 1;

		for (int i = 4; i < 10001; i++) {
			dp[i][1] = dp[i - 1][1];
			dp[i][2] = dp[i - 2][1] + dp[i - 2][2];
			dp[i][3] = dp[i - 3][1] + dp[i - 3][2] + dp[i - 3][3];
		}
	}

	public static void main(String[] args) throws Exception {
		solution();

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; i++) {
			int N = Integer.parseInt(br.readLine());
			System.out.println(dp[N][1] + dp[N][2] + dp[N][3]);
		}
	}
}