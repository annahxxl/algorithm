package 김태원.초급.해싱_and_파싱.회장_선거;

import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public String solution(String[] votes, int k) {
        Map<String, Set<String>> votersByCandidate = new HashMap<>();

        for (String s : votes) {
            String[] tmp = s.split(" ");
            String voter = tmp[0];
            String candidate = tmp[1];

            Set<String> voters = votersByCandidate.getOrDefault(candidate, new HashSet<>());
            voters.add(voter);
            votersByCandidate.put(candidate, voters);
        }

        Map<String, Integer> giftCounts = new HashMap<>();

        for (Map.Entry<String, Set<String>> entry : votersByCandidate.entrySet()) {
            Set<String> voters = entry.getValue();

            if (voters.size() >= k) {
                for (String voter : voters) {
                    giftCounts.put(voter, giftCounts.getOrDefault(voter, 0) + 1);
                }
            }
        }

        List<Map.Entry<String, Integer>> sortedGiftCounts =
                giftCounts.entrySet().stream()
                        .sorted(Map.Entry.<String, Integer>comparingByValue()
                                .reversed()
                                .thenComparing(Map.Entry.comparingByKey()))
                        .collect(Collectors.toList());

        return sortedGiftCounts.get(0).getKey();
    }

    public static void main(String[] args) {
        Solution T = new Solution();
        System.out.println(T.solution(new String[]{"john tom", "daniel luis", "john luis", "luis tom", "daniel tom", "luis john"}, 2));
        System.out.println(T.solution(new String[]{"john tom", "park luis", "john luis", "luis tom", "park tom", "luis john", "luis park", "park john", "john park", "tom john", "tom park", "tom luis"}, 2));
        System.out.println(T.solution(new String[]{"cody tom", "john tom", "cody luis", "daniel luis", "john luis", "luis tom", "daniel tom", "luis john"}, 2));
        System.out.println(T.solution(new String[]{"bob tom", "bob park", "park bob", "luis park", "daniel luis", "luis bob", "park luis", "tom bob", "tom luis", "john park", "park john"}, 3));
    }
}
