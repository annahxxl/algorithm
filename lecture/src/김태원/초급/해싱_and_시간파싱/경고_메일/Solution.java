package 김태원.초급.해싱_and_시간파싱.경고_메일;

import java.util.*;

class Solution {
    private int convertToMinutes(String time) {
        int h = Integer.parseInt(time.split(":")[0]);
        int m = Integer.parseInt(time.split(":")[1]);
        return h * 60 + m;
    }

    public String[] solution(String[] reports, int time) {
        Map<String, Integer> inTimes = new HashMap<>();
        Map<String, Integer> totalTimes = new HashMap<>();

        for (String report : reports) {
            String name = report.split(" ")[0];
            int minutes = convertToMinutes(report.split(" ")[1]);
            boolean isIn = report.split(" ")[2].equals("in") ? true : false;

            if (isIn) {
                inTimes.put(name, minutes);
                continue;
            }

            totalTimes.put(name, totalTimes.getOrDefault(name, 0) + (minutes - inTimes.get(name)));
        }

        List<String> answer = new ArrayList<>();

        for (String name : totalTimes.keySet()) {
            if (totalTimes.get(name) > time) answer.add(name);
        }

        answer.sort((a, b) -> a.compareTo(b));

        return answer.toArray(new String[0]);
    }

    public static void main(String[] args) {
        Solution T = new Solution();
        System.out.println(Arrays.toString(T.solution(new String[]{"john 09:30 in", "daniel 10:05 in", "john 10:15 out", "luis 11:57 in", "john 12:03 in", "john 12:20 out", "luis 12:35 out", "daniel 15:05 out"}, 60)));
        System.out.println(Arrays.toString(T.solution(new String[]{"bill 09:30 in", "daniel 10:00 in", "bill 11:15 out", "luis 11:57 in", "john 12:03 in", "john 12:20 out", "luis 14:35 out", "daniel 14:55 out"}, 120)));
        System.out.println(Arrays.toString(T.solution(new String[]{"cody 09:14 in", "bill 09:25 in", "luis 09:40 in", "bill 10:30 out", "cody 10:35 out", "luis 10:35 out", "bill 11:15 in", "bill 11:22 out", "luis 15:30 in", "luis 15:33 out"}, 70)));
        System.out.println(Arrays.toString(T.solution(new String[]{"chato 09:15 in", "emilly 10:00 in", "chato 10:15 out", "luis 10:57 in", "daniel 12:00 in", "emilly 12:20 out", "luis 11:20 out", "daniel 15:05 out"}, 60)));
    }
}
