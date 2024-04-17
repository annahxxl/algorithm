import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int N, K;
	static int max;
	static int[] nums;
	static int[] count = new int[100001];

	static int solution() {
		int[] count = new int[100001];
		int lp = 0, rp = 0, max = 0;

		while (rp < N) {
			int num = nums[rp];

			if (count[num] < K) {
				count[num]++;
				rp++;
			} else {
				count[nums[lp]]--;
				lp++;
			}

			max = Math.max(max, rp - lp);
		}

		return max;
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		nums = new int[N];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}

		int answer = solution();
		System.out.print(answer);
	}
}
