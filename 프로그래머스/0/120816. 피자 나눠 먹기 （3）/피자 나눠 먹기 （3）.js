function solution(slice, n) {
    let num=0;
    num=n/slice;
    if(n%slice!=0){
        num+=1;
    }
    
    return Math.trunc(num);
}