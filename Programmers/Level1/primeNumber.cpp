#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int solution(int n) {
    int answer = 0;
    int* arr = new int[n+1];
    
    for (int i = 2; i <= n; i++) 
        arr[i] = i;
    
    for (int i = 2; i <= sqrt(n); i++) {
        if (arr[i] == 0) continue;
        for (int j = 2 * i; j <= n; j += i)
            arr[j] = 0;
    }
    for (int i = 2; i <= n; i++) {
        if (arr[i] != 0) {
            answer++;
            cout << arr[i];
        }
    }
    delete arr;
    return answer;
}
int main() {
    solution(100);
}