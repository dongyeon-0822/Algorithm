class Solution {
    public long gcd(int a, int b) {
        if (b == 0) return a;
        else return gcd(b, a%b);
    }
    public long solution(int w, int h) {
        return (long) w * h - (w + h - gcd(w,h));
    }   
}