class Solution {
    public String solution(String cipher, int code) {
        char[] unit=cipher.toCharArray();
        String answer="";
        for(int i=code;i<=unit.length;i+=code){
            answer+=unit[i-1];
        }
        return answer;
    }
}