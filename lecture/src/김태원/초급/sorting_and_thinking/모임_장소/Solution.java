package 김태원.초급.sorting_and_thinking.모임_장소;

import java.util.*;

class Solution {
    public int solution(int[][] board) {
        int n = board.length;

        List<Integer> rows = new ArrayList<>();
        List<Integer> cols = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 1) {
                    rows.add(i);
                    cols.add(j);
                }
            }
        }

        cols.sort((a, b) -> a - b);
        int rowMid = rows.get(rows.size() / 2);
        int colMid = cols.get(cols.size() / 2);

        int answer = 0;
        for (int r : rows) answer += Math.abs(r - rowMid);
        for (int c : cols) answer += Math.abs(c - colMid);

        return answer;
    }

    public static void main(String[] args) {
        Solution T = new Solution();
        System.out.println(T.solution(new int[][]{{1, 0, 0, 0, 0}, {0, 0, 0, 0, 0}, {0, 0, 0, 0, 1}, {0, 0, 0, 0, 0}, {0, 0, 1, 0, 0}}));
        System.out.println(T.solution(new int[][]{{1, 0, 0, 0, 1}, {0, 0, 0, 0, 0}, {0, 0, 0, 0, 0}, {0, 0, 0, 0, 0}, {0, 0, 0, 1, 0}}));
        System.out.println(T.solution(new int[][]{{1, 0, 0, 0, 1, 1}, {0, 1, 0, 0, 1, 0}, {0, 1, 0, 0, 0, 0}, {0, 0, 0, 0, 1, 0}, {0, 0, 0, 0, 0, 1}, {1, 0, 0, 0, 1, 1}}));
    }
}
