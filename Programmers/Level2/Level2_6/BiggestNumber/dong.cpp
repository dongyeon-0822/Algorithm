#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(pair<string, int> a, pair<string, int> b) {
    return a.first > b.first;
}
string solution(vector<int> numbers) {
    string answer = "";
    vector<pair<string,int>> arr;
    string s = "";
    for (int i = 0; i < numbers.size(); i++) {
        if(to_string(numbers[i]).size() == 4)
            arr.push_back(make_pair(to_string(numbers[i]), 4));
        else if (to_string(numbers[i]).size() == 3) {
            s = to_string(numbers[i]);
            s += s[0];
            arr.push_back(make_pair(s, 3));
        }
        else if (to_string(numbers[i]).size() == 2) {
            s = to_string(numbers[i]);
            s += s[0]; s += s[1];
            arr.push_back(make_pair(s,2));
        }
        else {
            s = to_string(numbers[i]);
            s += s[0]; s += s[0]; s += s[0];
            arr.push_back((make_pair(s,1)));
        }
    }
    sort(arr.begin(), arr.end(), cmp);

    if (arr[0].first[0] == '0')
        answer = "0";
    else {
        for (int i = 0; i < arr.size(); i++)
            answer += arr[i].first.substr(0, arr[i].second);
    }
    return answer;
}
int main() {
    vector<int> numbers = { 10,101 };
    cout<<solution(numbers);
}