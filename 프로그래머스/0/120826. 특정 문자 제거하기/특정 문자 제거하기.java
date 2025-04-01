class Solution {
    public String solution(String my_string, String letter) {
     String answer="";
     char[] unit=my_string.toCharArray();
     for(int i=0;i<unit.length;i++){
         if(!String.valueOf(unit[i]).equals(letter)){
             answer+=unit[i];
         }
     }
        return answer;
      
    }
}