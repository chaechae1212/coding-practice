class Solution {
    public int solution(int hp) {
        int a=hp/5;
        int save = hp%5;
        int b = save/3;
        save = save%3;
        int c = save/1;
        return a+b+c;
        
    }
}