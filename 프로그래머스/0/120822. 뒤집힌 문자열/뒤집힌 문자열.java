class Solution {
    public String solution(String my_string) {
        char[] unit=my_string.toCharArray();
        int num=unit.length;
        String answer="";
        for(int i=num-1;i>=0;i--){
          answer+=unit[i];
       }
        return answer;
    }
}