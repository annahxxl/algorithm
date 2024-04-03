import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		// input
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int r = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());

		int[][] map = new int[r][c];

		for (int i = 0; i < r; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < c; j++) {
				int num = Integer.parseInt(st.nextToken());
				map[i][j] = num;
			}
		}

		// solution
		int[][] dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
		int[][] visited = new int[r][c];
		int[][] dis = new int[r][c];
		for (int[] row : dis) {
			Arrays.fill(row, -1);
		}

		Queue<int[]> q = new LinkedList<>();

		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (map[i][j] == 2) {
					visited[i][j] = 1;
					dis[i][j] = 0;
					q.add(new int[] {i, j});
				}
			}
		}

		while (!q.isEmpty()) {
			int[] cur = q.poll();
			int x = cur[0];
			int y = cur[1];

			for (int i = 0; i < 4; i++) {
				int nx = x + dir[i][0];
				int ny = y + dir[i][1];

				if (nx >= 0 && nx < r && ny >= 0 && ny < c && visited[nx][ny] == 0 && map[nx][ny] == 1) {
					visited[nx][ny] = 1;
					dis[nx][ny] = dis[x][y] + 1;
					q.add(new int[] {nx, ny});
				}
			}
		}

		// output
		StringBuilder sb = new StringBuilder();

		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (map[i][j] == 0) { // 갈 수 없는 땅은 0으로 출력
					sb.append("0 ");
				} else {
					sb.append(dis[i][j]).append(" ");
				}
			}
			sb.append("\n");
		}

		System.out.println(sb);
	}
}
