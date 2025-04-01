class Solution {
    public int solution(int[] array) {
       int count=0;
       for(int i=0;i<array.length;i++){
           String str=String.valueOf(array[i]);
           char[] unit=str.toCharArray();
           for(int j=0;j<unit.length;j++){
               if (unit[j]=='7'){
                   count++;
               }
           }
               
       }
        return count;
    }
}