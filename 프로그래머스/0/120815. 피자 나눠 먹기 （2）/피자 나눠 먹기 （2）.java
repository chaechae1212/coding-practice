class Solution {
    public int solution(int n) {
        int box=0;
        for(int i=1;i<=6*n;i++){
            if(i%6==0&&i%n==0){
                box=i;
                break;
            }
        }
        return box/6;
        
    }
}