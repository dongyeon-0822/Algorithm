#include <iostream>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

vector<int> arr;
void change_base(int n, int b) {
    int r;

    r = n % b;
    n /= b;
    if (n > 0) change_base(n, b);

    arr.push_back(r);
}
int solution(int n) {
    int answer = 0;

    change_base(n, 3);
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i];
    }
    for (int i = 0; i < arr.size(); i++) {
        answer += arr[i] * pow(3, i);
    }
    return answer;
}
int main() {
    printf("%d", solution(45));
}