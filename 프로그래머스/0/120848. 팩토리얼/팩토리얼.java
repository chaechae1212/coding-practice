class Solution {
    public int solution(int n) {
        int box=0;
        int answer = 0;
        int sum=1;
        for(int i=1;i<=n;i++){
            sum*=i;
            if(sum>n){
                return i-1;
            }
            else if(sum==n){
                return i;
            }
           
            }
        return 0;
    }
}