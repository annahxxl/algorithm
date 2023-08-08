import java.util.*;

class Solution {
    public int solution(int[][] lines) {
        int[] visited = new int[200];
        Arrays.fill(visited, 0);
        
        for (int[] line : lines) {
            int l = line[0];
            int r = line[1];

            for (int i = l; i < r; i++) {
                visited[i + 100]++;
            }
        }

        int count = 0;
        for (int v : visited) {
            if (v > 1) count++;
        }
        
        return count;
    }
}