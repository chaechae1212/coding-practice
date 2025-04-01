import java.util.ArrayList;

class Solution {
    public int solution(String my_string) {
        String[] arr=my_string.split(" ");
        int answer=Integer.parseInt(arr[0]);
        for(int i=1;i<arr.length;i+=2){
            if(arr[i].equals("+")){
                int num=Integer.parseInt(arr[i+1]);
                answer+=num;
            }
            else if(arr[i].equals("-")){
                int nnum=Integer.parseInt(arr[i+1]);
                answer-=nnum;
            }
        }
        return answer;
        
    }
}
