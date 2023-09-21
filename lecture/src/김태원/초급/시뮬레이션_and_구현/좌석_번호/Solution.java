package 김태원.초급.시뮬레이션_and_구현.좌석_번호;

import java.util.Arrays;

class Solution {
    public int[] solution(int c, int r, int k){
        int[] answer = new int[2];

        if (k > c * r) return answer;

        int[][] directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        int[][] grid = new int[c][r];
        int x = 0, y = 0, num = 1, dIdx = 0;

        while (num < k) {
            grid[y][x] = num;

            int nx = x + directions[dIdx][0];
            int ny = y + directions[dIdx][1];

            if (nx < 0 || nx >= r || ny < 0 || ny >= c || grid[ny][nx] > 0) {
                dIdx = (dIdx + 1) % 4;
                continue;
            }

            x = nx;
            y = ny;
            num++;
        }

        answer[0] = y + 1;
        answer[1] = x + 1;

        return answer;
    }

    public static void main(String[] args){
        Solution T = new Solution();
        System.out.println(Arrays.toString(T.solution(6, 5, 12)));
        System.out.println(Arrays.toString(T.solution(6, 5, 20)));
        System.out.println(Arrays.toString(T.solution(6, 5, 30)));
        System.out.println(Arrays.toString(T.solution(6, 5, 31)));
    }
}
