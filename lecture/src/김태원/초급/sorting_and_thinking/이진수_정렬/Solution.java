package 김태원.초급.sorting_and_thinking.이진수_정렬;

import java.util.Arrays;

class Solution {
    public int[] solution(int[] nums) {
        int n = nums.length;
        int[][] cnts = new int[n][2];

        for (int i = 0; i < n; i++) {
            int cnt = 0;
            int num = nums[i];
            int tmp = nums[i];

            while (tmp > 0) {
                if (tmp % 2 == 1) cnt++;
                tmp /= 2;
            }

            cnts[i][0] = cnt;
            cnts[i][1] = num;
        }

        Arrays.sort(cnts, (a, b) -> a[0] == b[0] ? a[0] - b[0] : a[1] - b[1]);

        int[] answer = new int[n];

        for (int i = 0; i < n; i++) {
            answer[i] = cnts[i][1];
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution T = new Solution();
        System.out.println(Arrays.toString(T.solution(new int[]{5, 6, 7, 8, 9})));
        System.out.println(Arrays.toString(T.solution(new int[]{5, 4, 3, 2, 1})));
        System.out.println(Arrays.toString(T.solution(new int[]{12, 5, 7, 23, 45, 21, 17})));
    }
}
