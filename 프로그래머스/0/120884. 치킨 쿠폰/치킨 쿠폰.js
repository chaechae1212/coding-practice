function solution(chicken) {
    let Chicken=0;
    let coupon=chicken;
    let serviceC=0;
    while(coupon>=10){
        serviceC=Math.trunc(coupon/10);
        coupon=serviceC+coupon%10
        Chicken+=serviceC;
        
    }
    return Chicken;
}