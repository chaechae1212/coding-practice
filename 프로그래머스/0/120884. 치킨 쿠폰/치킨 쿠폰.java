class Solution {
    public int solution(int chicken) {
        int coupon=chicken;
        int service_chicken=0;
        
        while(coupon>=10){
        service_chicken+=coupon/10;
        coupon=coupon/10+(coupon%10);
        
    }
        return service_chicken;
  }
}