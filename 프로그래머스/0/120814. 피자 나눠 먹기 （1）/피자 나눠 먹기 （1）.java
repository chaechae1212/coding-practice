class Solution {
    public int solution(int n) {
        int answer;
        int remain;
        answer=n/7;
        remain = n%7;
        if(remain>0){
            answer+=1;
        }
        return answer;
        
        
    }
}