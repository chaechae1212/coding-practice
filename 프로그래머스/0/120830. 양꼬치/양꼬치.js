function solution(n, k) {
    let price=n*12000+k*2000;
    let bal = Math.trunc(n/10);
    return price-bal*2000;
    
}