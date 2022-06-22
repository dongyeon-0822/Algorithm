#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int solution(string s) {
    int answer = 0;
    vector <int> results;
    string cmp, result;
    int count;

    for (int i = 1; i <= ceil((double)s.size() / 2); i++) { 
        cmp = s.substr(0, i);
        result = "";
        count = 1;
        for (int j = 1; j <= ceil((double)s.size() / i); j++) {
            if (s.size() < j * i) {
                result += cmp;
            }
            else {
                if (cmp == s.substr(j * i, i)) count++;
                else {
                    if (count != 1) result += to_string(count);
                    result += cmp;
                    cmp = s.substr(j * i, i);
                    count = 1;
                }
            }
        }
        results.push_back(result.size());
    }
    answer = *min_element(results.begin(), results.end());
    return answer;
}
int main() {
    cout << solution("aabbaccc");
}