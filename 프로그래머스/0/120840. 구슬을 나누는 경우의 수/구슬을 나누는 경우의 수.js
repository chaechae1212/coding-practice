function solution(balls, share) {
    let sum1=1;
    let sum2=1;
    for (let x=balls;x>=balls-share+1;x--){
      
        sum1*=x;
    }
    for(let y=1;y<=share;y++){
       
        sum2*=y;
    }
    return Math.round(sum1/sum2);
}