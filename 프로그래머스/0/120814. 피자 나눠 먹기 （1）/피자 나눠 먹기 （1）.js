function solution(n) {
    let num=0;
    num=Math.trunc(n/7)
    if(n%7!=0){
        num+=1;
    }
    return num;
}