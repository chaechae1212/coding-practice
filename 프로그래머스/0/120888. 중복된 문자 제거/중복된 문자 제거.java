class Solution {
    public String solution(String my_string) {
        char[] unit=my_string.toCharArray();
        String answer="";
        for (int i=0;i<unit.length;i++){
            if(!answer.contains(String.valueOf(unit[i]))){
                answer+=unit[i];
            }
        }
        return answer;
    }
}