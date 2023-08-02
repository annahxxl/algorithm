class Solution {
    public String solution(String polynomial) {
        int xNum = 0, constant = 0;
        
        for (String term : polynomial.split(" \\+ ")) {
            if (term.contains("x")) {
                xNum += term.equals("x") ? 1 : Integer.parseInt(term.substring(0, term.length() - 1));
                continue;
            }
            constant += Integer.parseInt(term);
        }
        
        return (xNum == 0 ? "" : (xNum == 1 ? "x" : xNum + "x")) +
            (constant == 0 ? "" : (xNum == 0 ? constant : " + " + constant));
    }
}