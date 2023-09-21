package 김태원.초급.시뮬레이션_and_구현.청소;

import java.util.*;

class Solution {
    public int[] solution(int[][] board, int k){
        int[] answer = new int[2];

        int n = board.length;
        int[][] directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        int dIdx = 0;
        int time = 0;
        int x = 0, y = 0;

        while (time < k) {
            time++;

            int nx = x + directions[dIdx][0];
            int ny = y + directions[dIdx][1];

            if (nx < 0 || nx >= n || ny < 0 || ny >= n || board[ny][nx] == 1) {
                dIdx = (dIdx + 1) % 4;
                continue;
            }

            x = nx;
            y = ny;
        }

        answer[0] = y;
        answer[1] = x;

        return answer;
    }

    public static void main(String[] args){
        Solution T = new Solution();
        int[][] arr1 = {{0, 0, 0, 0, 0},
                {0, 1, 1, 0, 0},
                {0, 0, 0, 0, 0},
                {1, 0, 1, 0, 1},
                {0, 0, 0, 0, 0}};
        System.out.println(Arrays.toString(T.solution(arr1, 10)));
        int[][] arr2 = {{0, 0, 0, 1, 0, 1},
                {0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 1},
                {1, 1, 0, 0, 1, 0},
                {0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0}};
        System.out.println(Arrays.toString(T.solution(arr2, 20)));
        int[][] arr3 = {{0, 0, 1, 0, 0},
                {0, 1, 0, 0, 0},
                {0, 0, 0, 0, 0},
                {1, 0, 0, 0, 1},
                {0, 0, 0, 0, 0}};
        System.out.println(Arrays.toString(T.solution(arr3, 25)));

    }
}