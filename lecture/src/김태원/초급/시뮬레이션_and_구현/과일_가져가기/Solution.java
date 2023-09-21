package 김태원.초급.시뮬레이션_and_구현.과일_가져가기;

class Solution {

    private int getMin(int[] cnts) {
        int min = Integer.MAX_VALUE;
        for (int c : cnts) {
            if (c < min) min = c;
        }
        return min;
    }

    private boolean hasUniqueMin(int[] cnts) {
        int min = getMin(cnts);
        int cnt = 0;
        for (int c : cnts) {
            if (c == min) cnt++;
        }
        return cnt == 1;
    }

    private int getMinIdx(int[] cnts) {
        int min = getMin(cnts);
        for (int i = 0; i < 3; i++) {
            if (cnts[i] == min) return i;
        }
        return 0;
    }

    public int solution(int[][] fruit) {
        int n = fruit.length;
        boolean[] exchanged = new boolean[n];

        for (int i = 0; i < n; i++) {
            if (exchanged[i]) continue;
            if (!hasUniqueMin(fruit[i])) continue;

            for (int j = i + 1; j < n; j++) {
                if (exchanged[j]) continue;
                if (!hasUniqueMin(fruit[j])) continue;

                int f1 = getMinIdx(fruit[i]);
                int f2 = getMinIdx(fruit[j]);

                if (f1 != f2 && fruit[j][f1] > 0 && fruit[i][f2] > 0) {
                    if (fruit[i][f1] + 1 <= fruit[i][f2] - 1 && fruit[j][f2] + 1 <= fruit[j][f1] + 1) {
                        fruit[i][f1]++;
                        fruit[i][f2]--;
                        fruit[j][f1]--;
                        fruit[j][f2]++;

                        exchanged[i] = true;
                        exchanged[j] = true;
                        break;
                    }
                }
            }
        }

        int answer = 0;

        for (int[] f : fruit) {
            answer += getMin(f);
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution T = new Solution();
        System.out.println(T.solution(new int[][]{{10, 20, 30}, {12, 15, 20}, {20, 12, 15}, {15, 20, 10}, {10, 15, 10}}));
        System.out.println(T.solution(new int[][]{{10, 9, 11}, {15, 20, 25}}));
        System.out.println(T.solution(new int[][]{{0, 3, 27}, {20, 5, 5}, {19, 5, 6}, {10, 10, 10}, {15, 10, 5}, {3, 7, 20}}));
        System.out.println(T.solution(new int[][]{{3, 7, 20}, {10, 15, 5}, {19, 5, 6}, {10, 10, 10}, {15, 10, 5}, {3, 7, 20}, {12, 12, 6}, {10, 20, 0}, {5, 10, 15}}));
    }

}
