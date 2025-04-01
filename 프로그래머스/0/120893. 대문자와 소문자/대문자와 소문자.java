class Solution {
    public String solution(String my_string) {
        String answer = "";
        char[] unit =my_string.toCharArray();
        for(int i=0;i<unit.length;i++){
            if(Character.isUpperCase(unit[i])){
                char k=Character.toLowerCase(unit[i]);
                answer+=k;
            }
            else if(Character.isLowerCase(unit[i])){
                char m=Character.toUpperCase(unit[i]);
                answer+=m;
            }
        }
        return answer;
    }
}