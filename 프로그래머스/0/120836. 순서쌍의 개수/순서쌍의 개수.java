class Solution {
    public int solution(int n) {
        int count=0;
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                if(i*j==n){
                    count++;
                }
                if(i*j>n){
                    break;
                }
            }
        }
        return count;
    }
}