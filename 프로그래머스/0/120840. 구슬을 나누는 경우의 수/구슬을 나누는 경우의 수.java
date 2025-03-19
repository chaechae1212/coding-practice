class Solution {
    public int solution(int balls, int share) {
        return combination(balls,share);
    }
    public int combination(int n,int r){
        if(r>n-r){
            r=n-r;
        }
        long result=1;
        
        for(int i=0;i<r;i++){
            result*=(n-i);
            result/=(i+1);
        }
        return (int)result;
    }
}