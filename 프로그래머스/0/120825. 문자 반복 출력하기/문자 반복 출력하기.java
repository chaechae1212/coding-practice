class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        char[] unit=my_string.toCharArray();
        for(int i=0;i<unit.length;i++){
            for(int j=1;j<=n;j++){
                answer+=unit[i];
            }
        }
        return answer;
    }
}