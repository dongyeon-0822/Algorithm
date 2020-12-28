#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> arr;
void change_base(int n) {
    int r = n % 3;
    n /= 3;
    if (r == 0) n -= 1;
    if (n > 0) change_base(n);

    if (r == 0) arr.push_back(4);
    else arr.push_back(r);
}
string solution(int n) {
    string answer = "";
    change_base(n);

    for (int i = 0; i < arr.size(); i++) {
        answer+= to_string(arr[i]);
    }
    return answer;
}