class Solution {
    public int solution(int chicken) {
        int coupon=chicken;
        int remember=0;
        while(coupon>=10){
      
        int service_chicken=coupon/10;
        remember+=service_chicken;
        coupon=service_chicken+(coupon%10);
        
    }
        return remember;
  }
}