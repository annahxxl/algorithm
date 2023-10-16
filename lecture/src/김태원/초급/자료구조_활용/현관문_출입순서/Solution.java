package 김태원.초급.자료구조_활용.현관문_출입순서;

import java.util.*;

class Solution {
    public int[] solution(int[] arrival, int[] state) {
        Queue<Integer> in = new LinkedList<>();
        Queue<Integer> out = new LinkedList<>();

        int n = arrival.length;
        int[] answer = new int[n];

        int second = 0;
        int prev = 1;
        int idx = 0;
        int cnt = 0;

        while (true) {
            if (idx < n && in.isEmpty() && out.isEmpty()) {
                if (second < arrival[idx]) {
                    second = arrival[idx];
                    prev = 1;
                }
            }

            while (idx < n && arrival[idx] == second) {
                if (state[idx] == 0) {
                    in.offer(idx);
                } else {
                    out.offer(idx);
                }
                idx++;
            }

            if (prev == 1) {
                if (!out.isEmpty()) {
                    answer[out.poll()] = second;
                    prev = 1;
                } else if (!in.isEmpty()) {
                    answer[in.poll()] = second;
                }
            } else if (prev == 0) {
                if (!in.isEmpty()) {
                    answer[in.poll()] = second;
                    prev = 0;
                } else if (!out.isEmpty()) {
                    answer[out.poll()] = second;
                    prev = 1;
                }
            }

            second++;
            cnt++;

            if (cnt == n) break;
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution T = new Solution();
        System.out.println(Arrays.toString(T.solution(new int[]{0, 1, 1, 1, 2, 3, 8, 8}, new int[]{1, 0, 0, 1, 0, 0, 1, 0})));
        System.out.println(Arrays.toString(T.solution(new int[]{3, 3, 4, 5, 5, 5}, new int[]{1, 0, 1, 0, 1, 0})));
        System.out.println(Arrays.toString(T.solution(new int[]{2, 2, 2, 3, 4, 8, 8, 9, 10, 10}, new int[]{1, 0, 0, 0, 1, 1, 0, 1, 1, 0})));
    }
}