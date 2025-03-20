class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer =new int[2];
        int a;
        int b;
        int box=0;
        for(int i=1;i<=denom1*denom2;i++){
            if(i%denom1==0&&i%denom2==0){
                box=i;
                break;
            }
            
        }
        a=box/denom1;
        b=box/denom2;
        denom1=denom1*a;
        denom2=denom2*b;
        
        numer1=numer1*a;
        numer2=numer2*b;
        answer[0]=numer1+numer2;
        answer[1]=denom1;
        
    int bo;
    bo=1;
        
    for(int k=denom1;k>=1;k--){
        if(answer[0]%k==0&&answer[1]%k==0){
            bo=k;
            break;
            
        }
   
    
    }
    answer[0]=answer[0]/bo;
    answer[1]=answer[1]/bo;
    return answer;
}}