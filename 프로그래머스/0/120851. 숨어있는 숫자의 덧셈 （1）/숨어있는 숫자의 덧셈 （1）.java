class Solution {
    public int solution(String my_string) {
        int answer=0;
        int realnum=0;
        char[] unit =my_string.toCharArray();
        for(char u:unit){
            if(Character.isDigit(u)){
               realnum = Character.getNumericValue(u);
                answer+=realnum;
                
            }
        }
        return answer;
    }
}