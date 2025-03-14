class Solution {
    public int solution(int n, int k) {
        int answer = n/10;
        int m = k-answer;
        return (n*12000+m*2000);
    }
}