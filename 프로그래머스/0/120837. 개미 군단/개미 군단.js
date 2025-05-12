function solution(hp) {
    let count=0;
    if(hp>=5){
    count +=Math.trunc(hp/5);
    hp=hp%5
    }
    if(hp>=3){
        count +=Math.trunc(hp/3);
        hp = hp%3;} 
    if(hp<3){
        count+=Math.trunc(hp/1);
        }
    return count
    
    
}