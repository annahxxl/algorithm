package 김태원.초급.sorting_and_thinking.최소_회의실_개수;

import java.util.*;

class Solution {
    public int solution(int[][] meetings) {

        List<int[]> list = new ArrayList<>();

        for (int meeting[] : meetings) {
            list.add(new int[]{meeting[0], 1}); // 시작 시간, 시작 여부
            list.add(new int[]{meeting[1], 0}); // 종료 시간, 시작 여부
        }

        Collections.sort(list, (a, b) -> {
            if (a[0] == b[0]) {
                return a[1] - b[1];
            }
            return a[0] - b[0];
        });

        int answer = 0;
        int cnt = 0;

        for (int[] meeting : list) {
            if (meeting[1] == 1) {
                cnt++;
            } else {
                cnt--;
            }

            answer = Math.max(answer, cnt);
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution T = new Solution();
        System.out.println(T.solution(new int[][]{{0, 10}, {20, 25}, {5, 15}, {2, 5}}));
        System.out.println(T.solution(new int[][]{{1, 30}, {2, 15}, {3, 10}, {4, 12}, {6, 10}}));
        System.out.println(T.solution(new int[][]{{3, 9}, {1, 10}, {5, 8}, {10, 15}, {9, 14}, {12, 14}, {15, 20}}));
        System.out.println(T.solution(new int[][]{{0, 5}, {2, 7}, {4, 5}, {7, 10}, {9, 12}}));
    }
}
