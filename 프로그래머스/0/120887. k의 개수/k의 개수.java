class Solution {
    public int solution(int i, int j, int k) {
        char targer=(char)(k+'0');
        int count=0;
        for(int h=i;h<=j;h++){
            String stri=String.valueOf(h);
            for(int p=0;p<stri.length();p++){
                if(stri.charAt(p)==targer){
                    count++;
                }
            }
        }
        return count;
    }
}