package 김태원.초급.비밀번호;

import java.util.*;

class Solution {
    public int solution(int[] keypad, String password) {
        int[][] pad = new int[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                pad[i][j] = keypad[i * 3 + j];
            }
        }

        int[][] dis = new int[10][10];
        for (int i = 0; i < 10; i++) {
            Arrays.fill(dis[i], 2);
            dis[i][i] = 0;
        }

        int[][] dir = {{-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}};
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                int from = pad[i][j];
                for (int k = 0; k < 8; k++) {
                    int nx = dir[k][0];
                    int ny = dir[k][1];
                    if (i + nx >= 0 && i + nx < 3 && j + ny >= 0 && j + ny < 3) {
                        int to = pad[i + nx][j + ny];
                        dis[from][to] = 1;
                    }
                }
            }
        }

        int answer = 0;
        for (int i = 1; i < password.length(); i++) {
            int from = (int) password.charAt(i - 1) - 48;
            int to = (int) password.charAt(i) - 48;
            answer += dis[from][to];
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution T = new Solution();
        System.out.println(T.solution(new int[]{2, 5, 3, 7, 1, 6, 4, 9, 8}, "7596218"));
        System.out.println(T.solution(new int[]{1, 5, 7, 3, 2, 8, 9, 4, 6}, "63855526592"));
        System.out.println(T.solution(new int[]{2, 9, 3, 7, 8, 6, 4, 5, 1}, "323254677"));
        System.out.println(T.solution(new int[]{1, 6, 7, 3, 8, 9, 4, 5, 2}, "3337772122"));
    }
}
