class Solution {
    public String solution(String my_string, int num1, int num2) {
        String answer = "";
        char box;
        char[] unit=my_string.toCharArray();
        box=unit[num1];
        unit[num1]=unit[num2];
        unit[num2]=box;
        for(int i=0;i<unit.length;i++){
           answer+=unit[i];
    }
        return answer;
    
}
}