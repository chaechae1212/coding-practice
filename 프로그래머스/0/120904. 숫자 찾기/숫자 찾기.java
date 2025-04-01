class Solution {
    public int solution(int num, int k) {
        String strnum=String.valueOf(num);
        char[] unit=strnum.toCharArray();
        String strk=String.valueOf(k);
        for(int i=0;i<unit.length;i++){
            String str=String.valueOf(unit[i]);
            if(str.equals(strk)){
                return i+1;
            }
        }
        return -1;
    }
}