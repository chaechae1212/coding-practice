function solution(n) {
    let sum=1;
    for(let i=1;i<=n;i++){
        sum=1;
        for(let j=1;j<=i;j++){
            sum*=j;
            if (sum==n){
                return i;
            }
            if(sum>n){
                return i-1;
            }
        }
    }
}