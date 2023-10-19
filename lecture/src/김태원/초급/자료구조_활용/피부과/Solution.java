package 김태원.초급.자료구조_활용.피부과;

import java.util.*;

class Solution {
    private int convertToMinutes(String time) {
        int h = Integer.parseInt(time.split(":")[0]);
        int m = Integer.parseInt(time.split(":")[1]);
        return h * 60 + m;
    }

    public int solution(int[] laser, String[] enter) {
        int n = enter.length;
        int[][] customers = new int[n][2];

        for (int i = 0; i < n; i++) {
            customers[i][0] = convertToMinutes(enter[i].split(" ")[0]);
            customers[i][1] = Integer.parseInt(enter[i].split(" ")[1]);
        }

        Queue<Integer> q = new LinkedList<>();
        int finishMinutes = customers[0][0];
        q.offer(customers[0][1]);

        int idx = 1;
        int answer = 0;

        for (int minutes = finishMinutes; minutes <= 1200; minutes++) {
            if (idx < n && minutes == customers[idx][0]) {
                if (q.isEmpty() && finishMinutes < minutes) {
                    finishMinutes = minutes;
                }
                q.offer(customers[idx][1]);
                idx++;
            }

            if (minutes == finishMinutes && !q.isEmpty()) {
                int type = q.poll();
                finishMinutes += laser[type];
            }

            answer = Math.max(answer, q.size());
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution T = new Solution();
        System.out.println(T.solution(new int[]{30, 20, 25, 15}, new String[]{"10:23 0", "10:40 3", "10:42 2", "10:52 3", "11:10 2"}));
        System.out.println(T.solution(new int[]{30, 20, 25, 15}, new String[]{"10:23 0", "10:40 3", "10:42 2", "10:52 3", "15:10 0", "15:20 3", "15:22 1", "15:23 0", "15:25 0"}));
        System.out.println(T.solution(new int[]{30, 20, 25, 15}, new String[]{"10:20 1", "10:40 1", "11:00 1", "11:20 1", "11:40 1"}));
    }
}
