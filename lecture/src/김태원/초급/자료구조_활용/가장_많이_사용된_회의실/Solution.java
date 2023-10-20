package 김태원.초급.자료구조_활용.가장_많이_사용된_회의실;

import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.TreeSet;

class Solution {
    public int solution(int n, int[][] meetings) {
        Arrays.sort(meetings, (a, b) -> a[0] - b[0]);

        TreeSet<Integer> rooms = new TreeSet<>();

        for (int i = 0; i < n; i++) {
            rooms.add(i);
        }

        Queue<int[]> uses = new PriorityQueue<>((a, b) -> a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]);
        int[] useCnts = new int[n];

        for (int[] meeting : meetings) {
            while (!uses.isEmpty() && uses.peek()[0] <= meeting[0]) {
                rooms.add(uses.poll()[1]);
            }

            if (rooms.isEmpty()) {
                int[] use = uses.poll();
                useCnts[use[1]]++;
                uses.add(new int[]{use[0] + (meeting[1] - meeting[0]), use[1]});
            } else {
                int room = rooms.pollFirst();
                useCnts[room]++;
                uses.add(new int[]{meeting[1], room});
            }
        }

        int answer = 0;
        int maxIdx = 0;

        for (int i = 0; i < n; i++) {
            if (useCnts[i] > maxIdx) {
                maxIdx = useCnts[i];
                answer = i;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution T = new Solution();
        System.out.println(T.solution(2, new int[][]{{0, 5}, {2, 7}, {4, 5}, {7, 10}, {9, 12}}));
        System.out.println(T.solution(3, new int[][]{{3, 9}, {1, 10}, {5, 8}, {10, 15}, {9, 14}, {12, 14}, {15, 20}}));
        System.out.println(T.solution(3, new int[][]{{1, 30}, {2, 15}, {3, 10}, {4, 12}, {6, 10}}));
        System.out.println(T.solution(4, new int[][]{{3, 20}, {1, 25}, {5, 8}, {10, 15}, {9, 14}, {12, 14}, {15, 20}}));
    }
}
