#include <iostream>
using namespace std;

int gcd(int a, int b) {
    if (b == 0) return a;
    else return gcd(b, a % b);
}

long long solution(int w, int h) {
    long long answer = 1;
    
    //큰수,작은수 나누기
    int max, min;
    if (w >= h) { max = w; min = h; }
    else { max = h; min = w; }

    int n = gcd(max, min);
    max /= n; min /= n;

    long sub = max + min - 1;
    answer = (long)w * h - sub * n;

    return answer;
}