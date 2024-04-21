import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int N, M;
	static Candy[] candies;
	static int[] dp;

	static int solution() {
		for (Candy candy : candies) {
			for (int i = candy.price; i <= M; i++) {
				dp[i] = Math.max(dp[i], dp[i - candy.price] + candy.calorie);
			}
		}

		return dp[M];
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		while (true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = (int)Math.round(Double.parseDouble(st.nextToken()) * 100);

			if (N == 0 && M == 0) {
				break;
			}

			candies = new Candy[N];
			dp = new int[M + 1];

			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				int C = Integer.parseInt(st.nextToken());
				int P = (int)Math.round(Double.parseDouble(st.nextToken()) * 100);

				candies[i] = new Candy(C, P);
			}

			System.out.println(solution());
		}
	}

	static class Candy {
		int calorie;
		int price;

		Candy(int calorie, int price) {
			this.calorie = calorie;
			this.price = price;
		}
	}
}
