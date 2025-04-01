class Solution {
    public int solution(String A, String B) {
        int num=A.length();
        String answer="";
        int save=-1;
        String rotated=A;
        if(A.equals(B)){
            return 0;
        }
        for(int i=1;i<num*2;i++){
            rotated=rotated.substring(num-1)+rotated.substring(0,num-1);
          
            if(B.equals(rotated)){
                save=i;
                break;
            }
        }
        return B.equals(rotated)?save:-1;
    }
}