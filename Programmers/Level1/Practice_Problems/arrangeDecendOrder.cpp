#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool desc(char a, char b) {
    return a > b;
}
long long solution(long long n) {
    long long answer = 0;
    vector<char> arr;

    string str = to_string(n);
    for (int i = 0; i < str.size(); i++) {
        arr.push_back(str[i]);
    }
    sort(arr.begin(), arr.end(), desc);
    string s = "";
    for (int i = 0; i < arr.size(); i++) {
        s += arr[i];
    }
    answer = stoll(s);
    return answer;
}