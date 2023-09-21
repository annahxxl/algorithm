package 김태원.초급.시뮬레이션_and_구현.잃어버린_강아지;

class Solution {
    public int solution(int[][] board){
        int n = board.length;
        int[][] directions = {{0, -1}, {1, 0}, {0, 1}, {-1, 0}};

        int x1 = 0, y1 = 0, d1 = 0;
        int x2 = 0, y2 = 0, d2 = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 2) {
                    x1 = j;
                    y1 = i;
                }

                if (board[i][j] == 3) {
                    x2 = j;
                    y2 = i;
                }
            }
        }

        int time = 0;

        while (time <= 10000) {
            time++;

            int nx1 = x1 + directions[d1][0];
            int ny1 = y1 + directions[d1][1];
            int nx2 = x2 + directions[d2][0];
            int ny2 = y2 + directions[d2][1];

            boolean turned1 = false, turned2 = false;

            if (nx1 < 0 || nx1 >= n || ny1 < 0 || ny1 >= n || board[ny1][nx1] == 1) {
                d1 = (d1 + 1) % 4;
                turned1 = true;
            }
            if (nx2 < 0 || nx2 >= n || ny2 < 0 || ny2 >= n || board[ny2][nx2] == 1) {
                d2 = (d2 + 1) % 4;
                turned2 = true;
            }
            if (!turned1) {
                x1 = nx1;
                y1 = ny1;
            }
            if (!turned2) {
                x2 = nx2;
                y2 = ny2;
            }

            if (x1 == x2 && y1 == y2) break;
        }

        return time >= 10000 ? 0 : time;
    }

    public static void main(String[] args){
        Solution T = new Solution();
        int[][] arr1 = {{0, 0, 0, 0, 0, 0, 1, 0, 0, 0},
                {0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
                {0, 0, 0, 1, 0, 0, 0, 1, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 1, 0, 0, 0, 2, 0, 0},
                {1, 0, 0, 0, 0, 0, 1, 0, 0, 0},
                {0, 0, 0, 1, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 3, 0, 0, 0, 1},
                {0, 0, 0, 1, 0, 1, 0, 0, 0, 0},
                {0, 1, 0, 1, 0, 0, 0, 0, 0, 0}};
        System.out.println(T.solution(arr1));
        int[][] arr2 = {{1, 0, 0, 0, 1, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 1, 0, 0, 0},
                {0, 0, 1, 1, 0, 0, 0, 1, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 1, 0, 1, 0, 0, 0, 0},
                {1, 0, 0, 0, 0, 0, 1, 0, 1, 0},
                {0, 0, 0, 1, 0, 0, 0, 0, 0, 0},
                {0, 0, 1, 0, 0, 0, 0, 0, 2, 1},
                {0, 0, 0, 1, 0, 1, 0, 0, 0, 1},
                {0, 1, 0, 1, 0, 0, 0, 0, 0, 3}};
        System.out.println(T.solution(arr2));
    }
}