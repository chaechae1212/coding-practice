function solution(price) {
    if(price>=500000){
        return Math.trunc(0.8*price);
    }
    
    if(price>=300000){
        return Math.trunc(0.9*price);
    }
    if(price>=100000){
        return Math.trunc(0.95*price);
    }
    else{
        return price;
    }
}