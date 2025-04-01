class Solution {
    public int solution(int order) {
        String stror=String.valueOf(order);
        char [] unit=stror.toCharArray();
        int count=0;
        for(int i=0;i<unit.length;i++){
            if(unit[i] == '3' || unit[i] == '6' || unit[i] == '9'){
                count++;
            }
        }
        return count;
        
    }
}