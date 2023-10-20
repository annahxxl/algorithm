package 김태원.초급.자료구조_활용.CPU_스케쥴링;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

class Solution {
    public int[] solution(int[][] tasks) {
        int n = tasks.length;

        LinkedList<int[]> programs = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            programs.add(new int[]{tasks[i][0], tasks[i][1], i});
        }

        programs.sort((a, b) -> a[0] - b[0]);

        Queue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]);
        int finishTime = 0;

        int[] answer = new int[n];
        int idx = 0;

        while (!programs.isEmpty() || !pq.isEmpty()) {
            if (pq.isEmpty()) {
                finishTime = Math.max(finishTime, programs.peek()[0]);
            }

            while (!programs.isEmpty() && programs.peek()[0] <= finishTime) {
                int[] program = programs.poll();
                pq.add(new int[]{program[1], program[2]});
            }

            int[] program = pq.poll();
            finishTime += program[0];
            answer[idx++] = program[1];
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution T = new Solution();
        System.out.println(Arrays.toString(T.solution(new int[][]{{2, 3}, {1, 2}, {8, 2}, {3, 1}, {10, 2}})));
        System.out.println(Arrays.toString(T.solution(new int[][]{{5, 2}, {7, 3}, {1, 3}, {1, 5}, {2, 2}, {1, 1}})));
        System.out.println(Arrays.toString(T.solution(new int[][]{{1, 2}, {2, 3}, {1, 3}, {3, 3}, {8, 2}, {1, 5}, {2, 2}, {1, 1}})));
        System.out.println(Arrays.toString(T.solution(new int[][]{{999, 1000}, {996, 1000}, {998, 1000}, {999, 7}})));
    }
}
